#! /usr/bin/python
# -*- coding: utf-8 -*-

#Script to convert 96-well plate format into column format. Data is from growth curves done on Tecan.
#updated 2024-08-26 so that growth curves of any length in time can be converted.
#updated 2024-11-06 so that single time points (like MICs) can also be read

import os
import pandas as pd
import numpy as np
import argparse

def main():

    parser = argparse.ArgumentParser(
		description = "This is script converts Tecan output csv data from 96-well plate format to column format. This is an updated script (2024-08-26) that allows growth curves of any length in time and takes in xlsx format as the input. It can also handle single time points.")

    parser.add_argument(
        '-i', '--input', 
        type=str, required=True,
        metavar="", 
        help='Name of the input filepath to a *.xlsx file. Required.')

    parser.add_argument(
		'-o', '--output',
        type=str,
		default = 'tecan_column-format',
        metavar="",
		help = "Name of the output filepath with file name. Defaults to './tecan_column-format.csv' in current directory if no output is assigned.")

    args = parser.parse_args()
    plate_df = pd.read_excel(args.input)
    
    # Ensure output file ends with ".csv"
    file_name = args.output if args.output.endswith(".csv") else args.output + ".csv"

    selected_data = []  # Create empty list for selected data

    # Retrieve every row index containing "<>" in the first column
    rows_with_bracket = plate_df[plate_df.iloc[:, 0] == "<>"].index.tolist()

    # Extract data around each "<>" row: 3 rows above and 8 rows below, 13 columns across
    for row in rows_with_bracket:
        selected_data.append(plate_df.iloc[row - 3:row + 9, :13])

    # Convert each DataFrame in selected_data to a numpy array and stack into a 3D array
    selected_data_3d = np.array([df.to_numpy() for df in selected_data])
    
    # Define column names for the output DataFrame
    number_of_blocks, rows, columns = selected_data_3d.shape
    well_labels = [f"{row}{col}" for row in 'ABCDEFGH' for col in range(1, 13)]
    
    # Create list to collect dictionaries for each block
    data_blocks = []

    # Populate data for each block, adding Time, Temp, Cycle if headers match
    for i, data_block in enumerate(selected_data):
        # Initialize block dictionary with well data
        block_data = {well_label: np.nan for well_label in well_labels}

        # Check if the expected headers are present above "<>"
        if (data_block.iloc[0, 0] == "Time [s]" and 
            data_block.iloc[1, 0] == "Temp. [°C]" and 
            data_block.iloc[2, 0] == "Cycle Nr."):
            # Add Time, Temp, Cycle if headers match
            block_data['Time'] = data_block.iloc[0, 1]  # time value
            block_data['Temp'] = data_block.iloc[1, 1]  # temp value
            block_data['Cycle'] = data_block.iloc[2, 1]  # cycle number

        for r, row_label in enumerate('ABCDEFGH', start=4):  # Start from row 4
            for c in range(1, 13):  # Columns 1-12
                well_label = f"{row_label}{c}"
                block_data[well_label] = data_block.iloc[r, c]
                
        # Append block data to list
        data_blocks.append(block_data)

    # Convert list of dictionaries to DataFrame
    column_df = pd.DataFrame(data_blocks)

    # Write the output DataFrame to a CSV file
    column_df.to_csv(file_name, index=False)

    # Inform the user of the output file location
    print(f"File has been written to: {os.path.abspath(file_name)}")



if __name__ == "__main__":
    main()