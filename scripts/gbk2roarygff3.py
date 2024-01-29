#! /usr/bin/python
# -*- coding: utf-8 -*-


#Written by Nanami Kubota

#converts Genbank (GBK) file into Roary-friendly GFF3+sequence file. Note that the phase column is empty. Proceed with caution if you plan to use the phase column.

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter, 
    description = "Tool that takes Genbank (GBK) file and converts to Roary-friendly GFF3+sequence file without having to use Prokka or Bakta")

parser.add_argument(
	'-i', '--input',
	action = "store",
    metavar = '',
	help = "Location of your Genbank file (GBK). Required.",
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

def gbk2roarygff3(input, output):
    with open(input, "r") as gbk_handle, open(output, "w") as gff3_handle:
        for record in SeqIO.parse(gbk_handle, "genbank"):
            genome_size = len(record.seq)
            # Write GFF3 header
            gff3_handle.write("##gff-version 3\n")s
            gff3_handle.write(f"##sequence-region\s{record.id}\t1\t{genome_size}\n")

            # Write sequence region line with custom format
            gff3_handle.write(f"{record.id}\tgbk2roarygff3\tregion\t1\t{genome_size}\t.\t"
                              f"{'+' if record.features[0].strand == 1 else '-'}\t.\t"
                              f"ID={record.id};Name={record.id};Is_circular=true\n")


            # Write GFF3 features (excluding 'gene')
            for feature in record.features:
                if feature.type != 'gene':
                    gene_name = feature.qualifiers.get('gene', [''])[0]
                    locus_tag = feature.qualifiers.get('locus_tag', [''])[0]
                    product = feature.qualifiers.get('product', [''])[0]

                    # If gene name is not present, use locus tag
                    if not gene_name:
                        gene_name = locus_tag
                    gff3_handle.write(f"{record.id}\tgbk2roarygff3\t{feature.type}\t"
                                      f"{feature.location.start + 1}\t{feature.location.end}\t.\t"
                                      f"{'+' if feature.strand == 1 else '-'}\t.\tID={locus_tag};Name={gene_name};Product={product}\n")

            # Write GFF3 sequence region
            gff3_handle.write(f"{record.id}\t.\tregion\t1\t{len(record.seq)}\t.\t.\t.\n")
            
            # Write sequence information in FASTA format
            gff3_handle.write("##FASTA\n")
            sequence = str(record.seq)
            gff3_handle.write(f">{record.id}\n")
            for i in range(0, len(sequence), 60):
                gff3_handle.write(sequence[i:i+60] + "\n")
    
    

if __name__ == "__main__":
    gbk2roarygff3(args.input, args.output)