#!/usr/bin/bash

#SBATCH --job-name=deffind
#SBATCH -w node02
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL

#written by Nanami Kubota

module purge
module load hmmer/hmmer-3.2.1
module load miniconda/miniconda-3

source /opt/miniconda/miniconda3/etc/profile.d/conda.sh
conda activate /home/nak177/defense_finder/defensefinder_env

defense-finder run /home/nak177/ref_seq/Pseudomonas_aeruginosa_MPAO1_15934.faa -o /home/nak177/defense_finder/MPAO1/

module purge