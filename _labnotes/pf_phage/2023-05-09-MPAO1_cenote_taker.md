---
title:  "MPAO1 Cenote-Taker2"
date: 2023-05-09
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: MPAO1 Pf4 and Pf6 run under cenote taker2 and 
---

<div class="notice--info">
  <b>Objective:</b> to map Pf4 and Pf6 region in MPAO1. 
  <ul>
    <li>Can map read depth across genome map later.</li>
  </ul>
</div>

Information on Cenote-Taker2: [https://github.com/mtisza1/Cenote-Taker2](https://github.com/mtisza1/Cenote-Taker2)

***
**2023-05-09**

Task:
- ran cenote taker on MPAO1 Pf4 and Pf6
- compare MPAO1 Pf4 and Pf6 with PAO1 Pf4 and other Pf phages

Script for running Cenote-Taker2:

```bash
#!/usr/bin/bash

#SBATCH --job-name=prophage_annotate
#SBATCH -w node02
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL

module purge
module load miniconda prodigal bowtie2 samtools/samtools-1.3.1 mummer bwa infernal bbtools tbl2asn spades

source /opt/miniconda/miniconda3/etc/profile.d/conda.sh
conda activate /home/nak177/cenote/cenote-taker2_env

python /home/nak177/cenote/Cenote-Taker2/run_cenote-taker2.py -c /home/nak177/ref_seq/MPAO1_Pf4.fna -r MPAO1_Pf4_DNA_ct -p False -am True -m 32 -t 32

python /home/nak177/cenote/Cenote-Taker2/run_cenote-taker2.py -c /home/nak177/ref_seq/MPAO1_Pf6.fna -r MPAO1_Pf6_DNA_ct -p False -am True -m 32 -t 32

module purge
```

Plot MPAO1 Pfs again PAO1 Pfs

***

**2023-06-15**

  