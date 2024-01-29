#!/usr/bin/bash

#SBATCH --job-name=deffind
#SBATCH -w node02
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL

#written by Nanami Kubota
#PA14 PAO1 defense finder run after updating defense finder

module purge
module load hmmer/hmmer-3.2.1
module load miniconda/miniconda-3

source /opt/miniconda/miniconda3/etc/profile.d/conda.sh
conda activate /home/nak177/defense_finder/defensefinder_env

defense-finder run /home/nak177/ref_seq/Pseudomonas_aeruginosa_PAO1_107.faa -o /home/nak177/defense_finder/PAO1_update/
defense-finder run /home/nak177/ref_seq/Pseudomonas_aeruginosa_UCBPP-PA14_109.faa -o /home/nak177/defense_finder/PA14_update/

module purge