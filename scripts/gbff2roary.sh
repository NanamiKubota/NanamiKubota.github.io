#!/usr/bin/bash

#SBATCH --job-name=gbk2roary
#SBATCH -w node02
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL

#written by Nanami Kubota

module purge
module load miniconda/miniconda-3

in_directory="/home/nak177/msa_comparison_tutorial/glenn"
out_directory="/home/nak177/msa_comparison_tutorial/glenn/roary_gff3"

# Check if the directory exists
if [ -d "$in_directory" ]; then
    # Loop through each .gbff file in the directory
    for file in "$in_directory"/*.gbff; do
        if [ -f "$file" ]; then
            # Get the filename without the path and extension
            filename=$(basename -- "$file")
            filename_no_extension="${filename%.*}"

            # Run the tool.py script and output to the "output" directory
            python3 /home/nak177/scripts/gbk2roarygff3.py -i "$file" -o "$out_directory"/"$filename_no_extension".gff3

            echo "Processed file: $file"
 
        fi
    done
else
    echo "Directory not found"
fi

module purge