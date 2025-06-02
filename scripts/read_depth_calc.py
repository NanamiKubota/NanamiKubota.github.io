#! /usr/bin/python
# -*- coding: utf-8 -*-

# After running breseq, this script will use the bam file to calculate read depth using samtools and bedtools
# Written by Nanami Kubota with help from ChatGPT

import argparse
import os
import subprocess
import tempfile
import shutil
from pathlib import Path

# Function to find all reference.bam files in input_dir and its subdirectories
def get_bam_files(input_dir):
    bam_files = []
    
    # Check if the input_dir is a file (single directory)
    if os.path.isfile(os.path.join(input_dir, "data", "reference.bam")):
        bam_files.append(os.path.join(input_dir, "data", "reference.bam"))
    
    # If the input_dir is a directory containing multiple subdirectories
    elif os.path.isdir(input_dir):
        for subdir in os.listdir(input_dir):
            subdir_path = os.path.join(input_dir, subdir)
            data_dir = os.path.join(subdir_path, "data")
            reference_bam = os.path.join(data_dir, "reference.bam")
            
            # If reference.bam file exists in the subdirectory, add to list
            if os.path.isfile(reference_bam):
                bam_files.append(reference_bam)

    return bam_files

# Function to calculate read depth
def read_depth_calc(reference_bam, window_size, temp_dir, read_depth_dir):
    # Get data directory
    data_dir = os.path.dirname(reference_bam)

    # Get reference.fasta.fai path
    reference_fasta_fai = os.path.join(data_dir, "reference.fasta.fai")

    # Create reference.txt file in temp directory
    reference_txt = temp_dir / "reference.txt"

    # Create a reference.txt file with contig names and lengths
    with open(reference_txt, "w") as temp_ref_txt:
        subprocess.run(
            [
                "awk",
                "-v", "OFS=\\t",
                "{print $1, $2}",
                reference_fasta_fai
            ],
            stdout=temp_ref_txt,
            check=True
        )

    # Create reference.windows.bed file in temp directory
    reference_windows_bed = temp_dir / "reference.windows.bed"
    with open(reference_windows_bed, "w") as temp_ref_win_bed:
        subprocess.run(
            [
                "bedtools", "makewindows",
                "-g", reference_txt,
                "-w", str(window_size)
            ],
            stdout=temp_ref_win_bed,
            check=True
        )

    # Create a read depth file
    read_depth_avg = temp_dir / "read_depth_avg.txt"
    with open(read_depth_avg, "w") as temp_read_depth_avg:
        # Create the command chain using Popen to pipe the output of samtools to awk
        samtools_process = subprocess.Popen(
            ["samtools", "depth", "-a", reference_bam],
            stdout=subprocess.PIPE,  # Pipe the output to awk
        )

        awk_process = subprocess.Popen(
            ["awk", f"{{sum+=$3}} (NR%{window_size})==0{{print sum/{window_size}; sum=0;}}"],
            stdin=samtools_process.stdout,  # Take input from samtools
            stdout=temp_read_depth_avg,  # Write the result to output file
        )

        # Close the samtools output stream to signal the end of data to awk
        samtools_process.stdout.close()

        # Wait for the awk process to complete
        awk_process.communicate()

    # Get the breseq directory name and set the final output file path
    breseq_name = os.path.basename(os.path.dirname(data_dir))
    read_depth_final = read_depth_dir / f"{breseq_name}_window_{window_size}.txt"

    # Combine the windows and depth data into a final output file
    with open(read_depth_final, "w") as final_output:
        subprocess.run(
            ["paste", reference_windows_bed, read_depth_avg],
            stdout=final_output,
            check=True
        )

    print(f"Read depth calculation completed for {breseq_name}. Output saved to {read_depth_final}")

# Parsing input directory and other arguments
parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter, 
    description = "Tool that calculates read depth from breseq bam file.  "
                    "Requires samtools and bedtools.  "
                    "Tested with samtools v1.21 and bedtools v2.26.0.  ")

parser.add_argument(
    '-d', '--directory',
    type=str,
    help = "Either the filepath of a main directory that contains subdirectories of each breseq run or the filepath of a single breseq run. Each breseq run directory should have a 'data' subdirectory which contains a 'reference.bam' file.",
    required=True
)

parser.add_argument(
    '-o', '--output',
    type=str,
    help = "Path of the output directory where a new 'read_depth' directory with read depth data will be created. Defaults to current directory.",
    default=os.getcwd()
)

parser.add_argument(
    '-w', '--window',
    type=int,
    help = "Window size increment to calculate read depth. Defaults to 10bp.",
    default=10
)

args = parser.parse_args()

input_dir = args.directory
output_dir = Path(args.output)
read_depth_dir = output_dir / 'read_depth'
window_size = args.window

# Create read_depth directory if it doesn't exist (including intermediate directories)
read_depth_dir.mkdir(parents=True, exist_ok=True)

# Create a temporary directory within the output directory
temp_dir = Path(tempfile.mkdtemp(dir=read_depth_dir))

# Ensure the temp directory is cleaned up even if an error occurs
try:
    # Check that input_dir exists and that it is a directory
    if not os.path.isdir(input_dir):
        print(f"Error: {input_dir} is not a valid directory.")
        exit(1)

    # Get a list of all reference.bam files (either from the single directory or multiple subdirectories)
    bam_files = get_bam_files(input_dir)

    # If there are bam files found, proceed with read depth calculation
    if bam_files:
        for reference_bam_path in bam_files:
            print(f"Found reference BAM file: {reference_bam_path}")
            read_depth_calc(reference_bam_path, window_size, temp_dir, read_depth_dir)
    else:
        print(f"No reference BAM file found in {input_dir} or its subdirectories.")

finally:
    # Remove the temporary directory after use
    shutil.rmtree(temp_dir)