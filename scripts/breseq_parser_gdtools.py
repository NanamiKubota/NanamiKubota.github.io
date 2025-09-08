#! /usr/bin/python
# -*- coding: utf-8 -*-

#Employs gdtools to convert breseq output to CSV file
#Written by Nanami Kubota

#update 2025-09-03: create temp dir to write temp files to rather than directly into breseq data dir


import os
import glob
import pandas as pd
import subprocess
from pathlib import Path
import argparse
import tempfile
import shutil

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

def make_tempdir_in_output(output_dir):
    tmpdir = tempfile.mkdtemp(dir=output_dir)
    print("Temporary directory created at:", tmpdir)
    return tmpdir

def annotate_gd_file(gd_file, ref_file, tmpdir):
    """Annotate a GD file using gdtools into tmpdir."""
    # use sample folder name + gd_file stem to avoid collisions
    sample_name = gd_file.parent.parent.name
    out = os.path.join(tmpdir, f"{sample_name}_{gd_file.stem}_annotated.tsv")
    subprocess.run(['gdtools', 'ANNOTATE', '-e', '-o', out, '-f', 'TSV', '-r', ref_file, gd_file], stdout=subprocess.DEVNULL)
    return out

def subtract_gd_file(gd_file, ancestor_file, ref_file, tmpdir):
    """Perform genome subtraction and annotate into tmpdir."""
    subout = os.path.join(tmpdir, f"{gd_file.stem}_subtract.gb")
    subprocess.run(['gdtools', 'SUBTRACT', '-o', subout, gd_file, ancestor_file], stdout=subprocess.DEVNULL)
    
    out = os.path.join(tmpdir, f"{gd_file.stem}_subtract.tsv")
    subprocess.run(['gdtools', 'ANNOTATE', '-e', '-o', out, '-f', 'TSV', '-r', ref_file, subout], stdout=subprocess.DEVNULL)
    return out

def collect_annotated_files(gd_file_map):
    """Collect and read all annotated TSV files in the given directory."""
    li = []
    for annotated_file, sample_name in gd_file_map.items():
        df = pd.read_csv(annotated_file, sep='\t', low_memory=False)
        df['breseq'] = sample_name  # original sample folder name
        li.append(df)
    return li

def process_gd_files(directory, ancestor=None, tmpdir=None):
    annotated_map = {}  # map tmp annotated file -> sample folder name

    for gdout in glob.glob(directory + '/**/data/output.gd', recursive=True):
        p = Path(gdout)
        ref = os.path.join(p.parent, "reference.gff3")
        sample_name = p.parents[1].name

        if ancestor is None:
            annotated_tsv = annotate_gd_file(p, ref, tmpdir)
        else:
            annotated_tsv = subtract_gd_file(p, ancestor, ref, tmpdir)

        annotated_map[annotated_tsv] = sample_name  # store each file

    li = collect_annotated_files(annotated_map)
    return li

def save_csv(dataframes, output, filename):
    """Save the concatenated dataframes as a CSV file."""
    dfs = pd.concat(dataframes, ignore_index=True)
    dfs.to_csv(os.path.join(output, filename + ".csv"), index=False)

def GD2CSV(directory, output, filename, ancestor):
    """Main function to process GD files and convert to CSV."""
    tmpdir = make_tempdir_in_output(output)
    
    try:
        dataframes = process_gd_files(directory, ancestor, tmpdir)
        save_csv(dataframes, output, filename)
    finally:
        # Clean up temp directory even if an error occurs
        if os.path.exists(tmpdir):
            shutil.rmtree(tmpdir)
            print(f"Temporary directory {tmpdir} removed")


if __name__ == "__main__":
    GD2CSV(args.directory, args.output, args.filename, args.ancestor)