#!/bin/bash

#SBATCH --job-name=parser
#SBATCH -w node02
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL

#load breseq
module load breseq/breseq-0.38.1
module load miniconda/miniconda-3


###breseq parser arguments
## d = directory that contains all breseq runs (required)
## o = output file destination (required)
## f = output filename (optional; defaults to 'breseq_output')
## a = directory of ancestor output.gd file (optional)

#parses without removing variant calls in ancestor
python /home/nak177/scripts/breseq_parser_gdtools.py -d /home/nak177/wgs/mpao1/breseq/ -o /home/nak177/wgs/mpao1/breseq/ -f breseq_parse

#removes and parses variant calls in ancestor from other samples
python /home/nak177/scripts/breseq_parser_gdtools.py -d /home/nak177/wgs/mpao1/breseq/ -o /home/nak177/wgs/mpao1/breseq/ -f breseq_parse_subtract -a /home/nak177/wgs/mpao1/breseq/breseq_1/data/output.gd

module purge