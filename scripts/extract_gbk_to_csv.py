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
        description = "This program converts Genbank files (.gbk) to csv format.  Use the csv output with R gggenes package to plot genome maps."
    )

    parser.add_argument(
        '-i', '--input', 
        type=str, required=True, 
        help='a *.gbk file or similar file format'
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        help="Name of the output filepath with file name. Defaults to './gbk_to_csv.csv' if no file name is assigned.",
        default='gbk_to_csv.csv'
    )

    args = parser.parse_args()

    file_name = args.output
    record = []

    # Use SeqIO.parse instead of SeqIO.read if there are multiple records
    for gb in SeqIO.parse(args.input, "genbank"):
        for feature in gb.features:
            if feature.type in ["CDS", "rRNA", "tRNA", "ncRNA"]:
                record.append(
                    {
                        'locus_tag': feature.qualifiers.get('locus_tag', [''])[0],
                        'gene': feature.qualifiers.get('gene', [''])[0],
                        'product': feature.qualifiers.get('product', [''])[0],
                        'start': feature.location.start,
                        'end': feature.location.end,
                        'strand': feature.location.strand
                    }
                )

    # Create DataFrame from collected records
    df = pd.DataFrame(record)
    df.to_csv(file_name, index=False)  # Write to CSV file without the index

if __name__ == "__main__":
    main()