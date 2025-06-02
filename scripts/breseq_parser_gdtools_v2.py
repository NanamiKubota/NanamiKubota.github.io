#! /usr/bin/python
# -*- coding: utf-8 -*-

#Employs gdtools to convert breseq output to CSV file
#Written by Nanami Kubota


import os
import glob
import pandas as pd
import subprocess
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter, 
    description = "Tool that parses breseq gdtools output files and coverts them to CSV.  "
                    "Please load breseq module and put all breseq output directories into one main directory.  " "Then run this script.  ")

parser.add_argument(
	'-d', '--directory',
	action = "store",
    metavar = '',
	help = "Location of your main directory that contains subdirectories of each breseq run. Each breseq subdirectory within this main directory should have a '/data/output'.gd file.",
	dest = "directory",
    required = True
)

parser.add_argument(
	'-o', '--output',
	action = "store",
    metavar = '',
	help = "Optional path of the output file. Defaults to current directory.",
    default=os.getcwd()
)

parser.add_argument(
	'-f', '--filename',
    metavar = '',
	help = "Name of the output file. Defaults to 'breseq_output.csv'",
    default = 'breseq_output'
)

parser.add_argument(
	'-a', '--ancestor',
    action = "store",
    metavar = '',
	help = "Optional input to add path to ancestor /data/output.gd file to subtract variant calls in the ancestor from the other variant call gd files"
)

args = parser.parse_args()

def annotate_gd_file(gd_file, ref_file):
    """Annotate a GD file using gdtools."""
    out = os.path.join(gd_file.parent, "annotated.tsv")
    subprocess.run(['gdtools', 'ANNOTATE', '-e', '-o', out, '-f', 'TSV', '-r', ref_file, gd_file], stdout=subprocess.DEVNULL)
    return out

def subtract_gd_file(gd_file, ancestor_file, ref_file):
    """Perform genome subtraction and annotate."""
    subout = os.path.join(gd_file.parent, "annotated_subtract.gb")
    subprocess.run(['gdtools', 'SUBTRACT', '-o', subout, gd_file, ancestor_file], stdout=subprocess.DEVNULL)
    
    out = os.path.join(gd_file.parent, "annotated_subtract.tsv")
    subprocess.run(['gdtools', 'ANNOTATE', '-e', '-o', out, '-f', 'TSV', '-r', ref_file, subout], stdout=subprocess.DEVNULL)
    return out

def collect_annotated_files(directory, pattern):
    """Collect and read all annotated TSV files in the given directory."""
    li = []
    for gdtsv in glob.glob(directory + pattern, recursive=True):
        p2 = Path(gdtsv)
        df = pd.read_csv(gdtsv, sep='\t', low_memory=False)
        df['breseq'] = p2.parents[1].relative_to(directory)
        li.append(df)
    return li

def process_gd_files(directory, ancestor=None):
    """Process all GD files: either annotate or subtract and annotate."""
    li = []
    for gdout in glob.glob(directory + '/**/data/output.gd', recursive=True):
        p = Path(gdout)
        ref = os.path.join(p.parent, "reference.gff3")
        
        if ancestor is None:
            annotated_tsv = annotate_gd_file(p, ref)
            li.extend(collect_annotated_files(directory, '/**/data/annotated.tsv'))
        else:
            annotated_tsv = subtract_gd_file(p, ancestor, ref)
            li.extend(collect_annotated_files(directory, '/**/data/annotated_subtract.tsv'))
    
    return li

def save_csv(dataframes, output, filename):
    """Save the concatenated dataframes as a CSV file."""
    dfs = pd.concat(dataframes, ignore_index=True)
    dfs.to_csv(os.path.join(output, filename + ".csv"), index=False)

def GD2CSV(directory, output, filename, ancestor):
    """Main function to process GD files and convert to CSV."""
    dataframes = process_gd_files(directory, ancestor)
    save_csv(dataframes, output, filename)


if __name__ == "__main__":
    GD2CSV(args.directory, args.output, args.filename, args.ancestor)