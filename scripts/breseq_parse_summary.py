#! /usr/bin/python
# -*- coding: utf-8 -*-

# Extracts summary stats from multiple breseq summary.html files and merges into a single csv file
# Written by Nanami Kubota

from bs4 import BeautifulSoup
import os
import pandas as pd
import glob
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="Tool that parses breseq summary.html files and merges them to a single CSV. "
                "Please module load breseq and put all breseq output directories into one main directory. "
                "Then run this script.")

parser.add_argument(
    '-d', '--directory',
    action="store",
    metavar='',
    help="Location of your main directory that contains subdirectories of each breseq run. Each breseq subdirectory "
         "within this main directory should have a 'output' directory with a 'summary.html' file.",
    dest="directory",
    required=True
)

parser.add_argument(
    '-o', '--output',
    action="store",
    metavar='',
    help="Path of the output file. Defaults to current directory.",
    default=os.getcwd()
)

parser.add_argument(
    '-f', '--filename',
    metavar='',
    help="Name of the output file. Defaults to 'breseq_summary_output_read_file_info.csv' and "
         "'breseq_summary_output_ref_seq_info.csv'",
    default='breseq_summary_output'
)

args = parser.parse_args()


# Function to open summary.html file and extract Read File Information table
def read_file_extract(summary_file):
    breseq_dir_name = os.path.basename(os.path.dirname(os.path.dirname(summary_file)))

    with open(summary_file, 'r') as read_file_html:
        read_file_soup = BeautifulSoup(read_file_html, 'html.parser')

        # Get column names and ignore the first one
        read_file_colnames = [col.get_text() for col in read_file_soup.find_all("table")[1].find("tr").find_all("th")][1:]
        read_file_colnames.append("breseq")  # Add 'breseq' column

        read_file_HTML_data = read_file_soup.find_all("table")[1].find_all("tr")[1:]

        # Get row data and ignore the first column
        read_file_summary_data = [
            [cell.get_text() for cell in row.find_all("td")][1:] + [breseq_dir_name]
            for row in read_file_HTML_data
        ]

    return read_file_colnames, read_file_summary_data


# Function to open summary.html file and extract Reference Sequence Information table
def ref_seq_extract(summary_file):
    breseq_dir_name = os.path.basename(os.path.dirname(os.path.dirname(summary_file)))

    with open(summary_file, 'r') as ref_seq_html:
        ref_seq_soup = BeautifulSoup(ref_seq_html, 'html.parser')

        # Get column names and ignore the first two
        ref_seq_colnames = [col.get_text() for col in ref_seq_soup.find_all("table")[2].find("tr").find_all("th")][2:]
        ref_seq_colnames.append("breseq")  # Add 'breseq' column

        ref_seq_HTML_data = ref_seq_soup.find_all("table")[2].find_all("tr")[1:]

        # Get row data and ignore the first two columns
        ref_seq_summary_data = [
            [cell.get_text() for cell in row.find_all("td")][2:] + [breseq_dir_name]
            for row in ref_seq_HTML_data
        ]

    return ref_seq_colnames, ref_seq_summary_data


def main(directory, output, filename):
    read_file_all_data = []
    ref_seq_all_data = []
    read_file_colnames, ref_seq_colnames = None, None

    # Process read file summary
    for read_file_summary_file in glob.iglob(os.path.join(directory, '**', 'output', 'summary.html'), recursive=True):
        read_file_colnames, read_file_summary_data = read_file_extract(read_file_summary_file)
        read_file_all_data.extend(read_file_summary_data)  # Combine data across all files

    # Make dataframe and clean data
    if read_file_all_data:
        read_file_df = pd.DataFrame(data=read_file_all_data, columns=read_file_colnames)

        # Ensure 'reads' column exists before processing
        if 'reads' in read_file_df.columns:
            read_file_df['reads'] = read_file_df['reads'].str.replace(',', '').astype(int)

        # Save dataframe as CSV
        read_file_output_path = os.path.join(output, filename + "_read_file_info.csv")
        read_file_df.to_csv(read_file_output_path, index=False)
        print(f"Saved file to: {read_file_output_path}")

    # Process reference sequence summary
    for ref_seq_summary_file in glob.iglob(os.path.join(directory, '**', 'output', 'summary.html'), recursive=True):
        ref_seq_colnames, ref_seq_summary_data = ref_seq_extract(ref_seq_summary_file)
        ref_seq_all_data.extend(ref_seq_summary_data)  # Combine data across all files

    # Make dataframe and clean data
    if ref_seq_all_data:
        ref_seq_df = pd.DataFrame(data=ref_seq_all_data, columns=ref_seq_colnames)

        # Ensure 'reads' column exists before processing
        if 'reads' in ref_seq_df.columns:
            ref_seq_df['reads'] = ref_seq_df['reads'].str.replace(',', '').astype(int)

        # Save dataframe as CSV
        ref_seq_output_path = os.path.join(output, filename + "_ref_seq_info.csv")
        ref_seq_df.to_csv(ref_seq_output_path, index=False)
        print(f"Saved file to: {ref_seq_output_path}")


if __name__ == "__main__":
    main(args.directory, args.output, args.filename)
