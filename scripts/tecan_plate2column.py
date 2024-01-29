#! /usr/bin/python
# -*- coding: utf-8 -*-

#Script to convert 96-well plate format into column format. Data is from growth curves done on Tecan.
#written by Nanami Kubota

import os
import pandas as pd
import argparse

def main():

    parser = argparse.ArgumentParser(
		description = "This is script converts Tecan output csv data from 96-well plate format to column format.")

    parser.add_argument(
        '-i', '--input', 
        type=str, required=True,
        metavar="", 
        help='Name of the input filepath to a *.csv file. Required.')

    parser.add_argument(
		'-o', '--output',
        type=str,
		default = 'tecan',
        metavar="",
		help = "Name of the output filepath with file name. Defaults to writing './tecan_column-format_label1.csv' and './tecan_column-format_label2.csv' in current directory if no output is assigned.")
    
    parser.add_argument(
        '-t', '--timepoints',
        type=int,
        required=True,
        metavar="",
        help = "Total number of time points taken through the whole duration of the growth curve. Use integers."
    )

    args = parser.parse_args()

    label1 = pd.read_csv(args.input, encoding='latin1', skiprows=51, header=None)[:-37]
    #label2 = pd.read_csv(args.input, encoding='latin1', skiprows=1956, header=None)[:-4]

    file_name = args.output

    arr1 = label1.values.reshape(145, 13, 13)
    #arr2 = label2.values.reshape(145, 13, 13)
    
    list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    list2 = range(1,13)
    colname = [x + str(y) for x in list1 for y in list2]
    colname.insert(0,'Cycle')
    colname.insert(1,'Time')

    column_df1 = pd.DataFrame(columns = [colname])
    #column_df2 = pd.DataFrame(columns = [colname])

    column_df1['Cycle'] = list(map(int, arr1[:,2,1]))
    #column_df2['Cycle'] = list(map(int, arr1[:,2,1]))
    column_df1['Time'] = list(map(float, arr1[:,0,1]))
    #column_df2['Time'] = list(map(float, arr1[:,0,1]))

    k = 2
    for i in range(4,12):
        for j in range(1,13):
            #print(k)
            column_df1.iloc[:,k] = list(map(float, arr1[:,i,j]))
            #column_df2.iloc[:,k] = list(map(float, arr2[:,i,j]))
            k += 1

    column_df1.to_csv(file_name + "_column-format_label1.csv", index=False)
    #column_df2.to_csv(file_name + "_column-format_label2.csv", index=False)

if __name__ == "__main__":
    main()