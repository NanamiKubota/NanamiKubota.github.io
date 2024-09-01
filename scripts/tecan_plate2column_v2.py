#! /usr/bin/python
# -*- coding: utf-8 -*-

#Script to convert 96-well plate format into column format. Data is from growth curves done on Tecan.
#updated 2024-08-26 so that growth curves of any length in time can be converted.

import os
import pandas as pd
import numpy as np
import argparse

def main():

    parser = argparse.ArgumentParser(
		description = "This is script converts Tecan output csv data from 96-well plate format to column format. This is an updated script (2024-08-26) that allows growth curves of any length in time and takes in xlsx format as the input.")

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
		help = "Name of the output filepath with file name. Defaults to writing './tecan_column-format.csv' in current directory if no output is assigned.")

    args = parser.parse_args()
    plate_df = pd.read_excel(args.input)

    file_name = args.output

    selected_data = [] #create empty list

    #in the tecan raw data, retrieve every row number with "Time [s]" 
    rows_with_time = plate_df[plate_df.iloc[:, 0] == "Time [s]"].index.tolist()

    #extract plate data (i.e. 12 rows down from the "Time [s]" cell and 13 columns over) as a dataframe for every instance of "Time [s]" and append to selected_data
    for row in rows_with_time:
        selected_data.append(plate_df.iloc[row:row + 12, :13])

    #convert each dataFrame in selected_data to a numpy array and stack them into a 3D array
    selected_data_3d = np.array([df.to_numpy() for df in selected_data])
    
    #make empty column-format dataframe to populate
    number_of_blocks, rows, columns = selected_data_3d.shape
    list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    list2 = range(1,13)
    colname = [x + str(y) for x in list1 for y in list2]
    colname.insert(0,'Time')
    colname.insert(1, 'Temp')
    colname.insert(2,'Cycle')
    column_df = pd.DataFrame(index=range(number_of_blocks), columns = [colname])

    #loop to populate first three columns (time, temp, and cycle)
    for i in range(number_of_blocks):
        for r in range(rows):
            if r == 0:
                column_df.iloc[i,0] = selected_data_3d[i,0,1] #time column
            elif r == 1:
                column_df.iloc[i,1] = selected_data_3d[i,1,1] #temp column
            elif r == 2:
                column_df.iloc[i,2] = selected_data_3d[i,2,1] #cycle column

    #loop to populate plate reader data from plate-format to column-format
    k=3 #to start from column index 3
    for a in range(4,12):
        for c in range(1,13):
            column_df.iloc[:,k] = list(map(float, selected_data_3d[:,a,c]))
            k += 1

    column_df.to_csv(file_name + ".csv", index=False)

if __name__ == "__main__":
    main()