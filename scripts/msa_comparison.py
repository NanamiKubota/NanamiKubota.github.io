#! /usr/bin/python
# -*- coding: utf-8 -*-


#Written by Nanami Kubota

## multiple sequence alignments (MSAs) of loci of interest across different strains
#output 1: a csv file indicating the differences in amino acid sequence between your "reference strain" and other strains
#output 2: fasta file(s) containing MSA. These can be plotted in R using the ggmsa package.
#files required: genbank files and roary output file

import argparse
import os
import glob
import pandas as pd
import subprocess
from Bio import SeqIO, AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline
from io import StringIO

parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter, 
    description = "Tool that uses homologous loci identified by roary to conduct multiple sequence alignments. "
                    "Outputs a csv file indicating all the differences between the references strain and other strains. "
                    "Also outputs a MSA file in fasta format for each locus. ")

parser.add_argument(
    '-g', '--genbank',
    action = "store",
    metavar = '',
    help = "Location of your directory that contains the Genbank file (gbk or gbff) of each strain to be aligned. Required.",
    required = True
)

parser.add_argument(
    '-f', '--format',
    action = "store",
    help = "format of the genbank input file (gbk or gbff). Defaults to gbk.",
    choices = ['gbk', 'gbff'],
    default = 'gbk'
)

parser.add_argument(
    '-r', '--roary',
    action = "store",
    metavar = '',
    help = "Filepath to your roary gene_presence_absence.csv output file. Required.",
    required = True
)

parser.add_argument(
    '-ref', '--reference',
    type=str,
    metavar = '',
    help = "The name of your reference strain",
    required = True
)

parser.add_argument(
    '-l', '--loci',
    action = "store",
    metavar = '',
    help = "The csv file containing a list of loci to MSA",
    required = True
)

parser.add_argument(
    '-o', '--output',
    action = "store",
    metavar = '',
    help = "Path of the output file. Required.",
    required = True
)


args = parser.parse_args()

def msa_comparison(genbank, format, roary, reference, loci, output):
    
    alignment_path = os.path.join(output, 'alignment') #path to alignment output file that will house msa fasta files
    
    #check if alignment file already exist in output directory
    if os.path.exists(alignment_path):

        print(f"Directory '{alignment_path}' already exists. Please either choose a different output directory or rename your current alignment directory to avoid overwriting it.")

    else:
        
        os.makedirs(alignment_path) #create alignment directory

        directory_path = os.path.abspath(genbank) #find path to genbank files
        matching_files = glob.glob(os.path.join(directory_path, f"*.{format}")) #find filepaths of all genbank files with specified file extension. defaults to gbk.

        # create empty list to loop through each genbank file + append genbank records
        genbank_records = []
        for genbank_file in matching_files:
            # append each record to list
            print("Reading " + os.path.splitext(os.path.basename(genbank_file))[0] + " Genbank file")
            for record in SeqIO.parse(genbank_file, "genbank"):
                record.strain = os.path.splitext(os.path.basename(genbank_file))[0]
                genbank_records.append(record)

        print("All Genbank files read.")
        
        
        loci_csv = pd.read_csv(loci) # read csv file with list of loci
        ref_locus_tags = loci_csv["locus_tags"] #list of target ref locus

        roary_csv = pd.read_csv(roary) #read roary csv
        avg_group_size_index = roary_csv.columns.get_loc("Avg group size nuc") #find the index of the "Avg group size nuc" column
        selected_columns = roary_csv.columns[avg_group_size_index + 1:] #grab columns after the "Avg group size nuc" column (i.e. columns with locus tags of strains relative to each other)

        #check if reference is in roary column name
        if reference in roary_csv.columns:
            #if reference if in roary csv column name, loop through desired reference locus tags and find homolog in other strains using roary csv
            
            data_to_append = [] #create empty list to append msa dataframe for csv conversion later

            for ref_locus_tag in ref_locus_tags:
                row_index = roary_csv[roary_csv[reference] == ref_locus_tag].index[0] #find index of first locus tag in roary csv
                matching_rows = roary_csv.loc[row_index, selected_columns] #grab locus tags of all strains from index row
                roary_vector = matching_rows.to_numpy() #convert locus tags of all strains to vector
                print("Preparing to extract amino acid sequences for:")
                print(ref_locus_tag) #print reference locus tag
                
                # grab aa sequence from genbank files and save it in amino_acid_sequence (the temp input file to do msa on)
                amino_acid_sequence = "" 
                for record in genbank_records:
                    strain = record.strain
                    for feature in record.features:
                        if feature.type == "CDS":
                            if "translation" in feature.qualifiers and "locus_tag" in feature.qualifiers:
                                if feature.qualifiers["locus_tag"][0] in roary_vector:
                                    content = f">{strain}\n"
                                    amino_acid_record = feature.qualifiers["translation"][0]
                                    content_aa = f"{amino_acid_record}\n"
                                    amino_acid_sequence = amino_acid_sequence + content + content_aa

            
                count_gt = amino_acid_sequence.count(">") #check how many genome(s) are in amino acid sequence fasta, only do MSA on files with more than 1 genome
            
                if count_gt < 2:
                    print(f"No homologous locus found for '{ref_locus_tag}' and unable to MSA as a result. Moving onto next locus tag.")
                else:
                    print("Creating temp input file")

                    input_fasta = os.path.join(alignment_path, "temp_input.fasta") #add a line later to remove temp files

                    with open(input_fasta, "w") as file:
                        file.write(amino_acid_sequence) #create temp input fasta file (overwrites previous temp input file for each locus tag)

                    print("Preparing to run clustal omega")
                    
                    output_aln = os.path.join(alignment_path, f"{ref_locus_tag}_aligned.fasta") #output path for msa file for each locus tag

                    clustalomega_cline = ClustalOmegaCommandline(infile=input_fasta, outfile=output_aln, verbose=True, auto=True, force=True)

                    subprocess.run(str(clustalomega_cline), shell=True) #run clustalomega to do msa

                    print("finished writing output clustal omega file for " + ref_locus_tag)
                    
                    

                    msa = AlignIO.read(output_aln, "fasta") #read msa alignment fasta file

                    # find reference sequence
                    reference_seq = None
                    for record in msa:
                        if record.id == reference:
                            reference_seq = record.seq
                            break
                    
                    data = [] #empty list for single msa comparison, append this to data_to_append at the end
                    
                    # loop through each sequence and find base changes from reference strain
                    for record in msa:
                        # Skip the reference strain itself
                        if record.id == reference:
                            continue
                        compared_seq = record.seq
                        
                        # base_changes = []

                        # find base changes
                        for position, (a, b) in enumerate(zip(reference_seq, compared_seq)):
                            if a != b:
                                data.append({
                                    "Ref_locus": ref_locus_tag,
                                    "Strain_ID": record.id,
                                    "AA_Position": position + 1,  # Adding 1 to make it 1-based position
                                    "Ref_AA": f"{a}",
                                    "Strain_AA": f"{b}"
                                })
                        
                        # data.append(base_changes)# append base changes to data_to_append

                    data_to_append.append(data)# append base changes to data_to_append

            # create dataframe from the list of data
            flattened_data = [item for sublist in data_to_append for item in sublist]
            data_all = pd.DataFrame(flattened_data)

            # save dataframe as csv
            output_csv = os.path.join(output, "output_data.csv")
            data_all.to_csv(output_csv, index=False)
            print(f"Results saved to: {output_csv}")
            

        else:
            print(f"Error: either your reference strain name, '{reference}', does not match with its corresponding column name in the Roary output file or '{reference}' does not exist in the Roary output file.")



if __name__ == "__main__":
    msa_comparison(args.genbank, args.format, args.roary, args.reference, args.loci, args.output)