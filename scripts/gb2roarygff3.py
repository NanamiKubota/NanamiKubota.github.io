#! /usr/bin/python
# -*- coding: utf-8 -*-


#Written by Nanami Kubota

#converts Genbank (GBK or GBFF) file into Roary-friendly GFF3+sequence file. Note that the phase column is empty. Proceed with caution if you plan to use the phase column.

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter, 
    description = "Tool that takes Genbank (GBK or GBFF) file and converts to Roary-friendly GFF3+sequence file without having to use Prokka or Bakta")

parser.add_argument(
	'-i', '--input',
	action = "store",
    metavar = '',
	help = "Location of your Genbank file (GBK or GBFF). Required.",
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

def gb2roarygff3(input, output):
    with open(input, "r") as gb_handle, open(output, "w") as gff3_handle:
        for record in SeqIO.parse(gb_handle, "genbank"):
            genome_size = len(record.seq)
            #write GFF3 header
            gff3_handle.write("##gff-version 3\n")
            gff3_handle.write(f"##sequence-region\t{record.id}\t1\t{genome_size}\n")

            #write sequence region line with custom Roary-acceptable format
            gff3_handle.write(f"{record.id}\tgb2roarygff3\tregion\t1\t{genome_size}\t.\t"
                              f"{'+' if record.features[0].location.strand == 1 else '-'}\t.\t"
                              f"ID={record.id};Name={record.id}\n")


            #write GFF3 features (excluding 'gene')
            for feature in record.features:
                if feature.type not in ['gene', 'source']:
                    gene_name = feature.qualifiers.get('gene', [''])[0]
                    locus_tag = feature.qualifiers.get('locus_tag', [''])[0]
                    product = feature.qualifiers.get('product', [''])[0]

                    #if gene name is not present, use locus tag instead
                    if not gene_name:
                        gene_name = locus_tag
                    gff3_handle.write(f"{record.id}\tgb2roarygff3\t{feature.type}\t"
                                      f"{feature.location.start + 1}\t{feature.location.end}\t.\t"
                                      f"{'+' if feature.location.strand == 1 else '-'}\t.\tID={locus_tag};Name={gene_name};Product={product}\n")

            #write GFF3 sequence region
            gff3_handle.write(f"{record.id}\t.\tregion\t1\t{len(record.seq)}\t.\t.\t.\n")
            
            #write sequence information in FASTA format
            gff3_handle.write("##FASTA\n")
            sequence = str(record.seq)
            gff3_handle.write(f">{record.id}\n")
            for i in range(0, len(sequence), 60):
                gff3_handle.write(sequence[i:i+60] + "\n")
    
    

if __name__ == "__main__":
    gb2roarygff3(args.input, args.output)