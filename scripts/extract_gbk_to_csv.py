#! /usr/bin/python
# -*- coding: utf-8 -*-

#script to extract locus tags, gene name, product name, and start/end sites of ORFs from .gbk file
#written by Nanami Kubota

import os
from Bio import SeqIO
import pandas as pd
import re
import argparse

def main():

    parser = argparse.ArgumentParser(
		description = "This is program converts Genbank files (.gbk) to csv format.  Use the csv output with R gggenes package to plot genome maps.  ")

    parser.add_argument(
        '-i', '--input', 
        type=str, required=True, 
        help='a *.gbk file or similar file format'
    )
    
    parser.add_argument(
		'-o', '--output',
        type=str,
		help = "Name of the output filepath with file name. Defaults to './gbk_to_csv.csv' if no file name is assigned.",
		default = 'gbk_to_csv.csv'
	)

    args = parser.parse_args()
    
    gb = SeqIO.read(args.input, "genbank")

    file_name = args.output
    
    record = []
    
    for feature in gb.features:
        if feature.type == "CDS" or feature.type == "rRNA" or feature.type == "tRNA" or feature.type == "ncRNA":
            record.append(
                {
                    'locus_tag': re.sub(r"[\['\]']", "", str(feature.qualifiers.get('locus_tag'))),
                    'gene':  re.sub(r"[\['\]']", "", str(feature.qualifiers.get('gene'))),
                    'product': re.sub(r"[\['\]']", "", str(feature.qualifiers.get('product'))),
                    'start': feature.location.start,
                    'end': feature.location.end,
                    'strand': feature.location.strand
                }
            )
    
    df = pd.DataFrame(record)
    df.to_csv(file_name + ".csv")

if __name__ == "__main__":
    main()