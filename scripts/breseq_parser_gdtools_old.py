#! /usr/bin/python
# -*- coding: utf-8 -*-

import pathlib
from pathlib import Path
import argparse
from argparse import RawTextHelpFormatter
import os
import glob
import pandas as pd
import subprocess

parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter, 
    description = "Tool that parses breseq gdtools output files and coverts them to CSV.  "
                    "Please load breseq module and put all breseq output directories into one main directory.  " "Then run this script.  ")

parser.add_argument(
	'-d', '--directory',
	action = "store",
	help = "Location of your main directory that contains subdirectories of each breseq run. Each breseq subdirectory within this main directory should have a /data/output.gd file.",
	dest = "directory",
    required = True
)

parser.add_argument(
	'-o', '--output',
	action = "store",
	help = "Name of the output file. Defaults to './breseq_output.csv'",
)

args = parser.parse_args()

def GD2CSV(directory, output):
    for gdout in glob.glob(directory + '/**/data/output.gd', recursive=True):
        p = Path(gdout)
        ref = os.path.join(p.parent, "reference.gff3")
        out = os.path.join(p.parent, "annotated.tsv")
        subprocess.run(['gdtools', 'ANNOTATE', '-e', '-o', out, '-f', 'TSV', '-r', ref, p], stdout=subprocess.DEVNULL)
    li = []
    for gdtsv in glob.glob(directory + '/**/data/annotated.tsv', recursive=True):
        p2 = Path(gdtsv)
        df = pd.read_table(gdtsv, sep='\t')
        df['breseq'] = p2.parents[1].relative_to(directory)
        li.append(df)
    dfs = pd.concat(li, ignore_index=True)
    dfs.to_csv(os.path.join(output, "breseq_all.csv"), index=False)

if __name__ == "__main__":
    GD2CSV(args.directory, args.output)