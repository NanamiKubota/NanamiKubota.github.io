---
title: "Analyzing and plotting read depth data from breseq output"
layout: single
permalink: /tutorials/read_depth
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2022-10-14
#classes: wide
---

> Note: This is a tutorial was made for the purposes of extracting read depth data after running and obtaining breseq output(s) on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

***

# Getting started

```bash
#!/bin/bash

#SBATCH --job-name=read_depth
#SBATCH -w node02
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL

module purge
module load samtools bedtools

samtools faidx /home/nak177/burk_pa/breseq_rerun/breseq_01_rerun/data/reference.fasta

awk -v OFS='\t' {'print $1,$2'} /home/nak177/burk_pa/breseq_rerun/breseq_01_rerun/data/reference.fasta.fai > /home/nak177/burk_pa/breseq_rerun/read_depth/reference.txt

bedtools makewindows -g /home/nak177/burk_pa/breseq_rerun/read_depth/reference.txt -w 10 > /home/nak177/burk_pa/breseq_rerun/read_depth/reference.windows.bed

samtools depth -a /home/nak177/burk_pa/breseq_rerun/breseq_01_rerun/data/reference.bam | awk '{sum+=$3} (NR%10)==0{print sum/10; sum=0;}' > /home/nak177/burk_pa/breseq_rerun/read_depth/breseq_01_cov_10a.txt

paste /home/nak177/burk_pa/breseq_rerun/read_depth/reference.windows.bed /home/nak177/burk_pa/breseq_rerun/read_depth/breseq_01_cov_10a.txt > /home/nak177/burk_pa/breseq_rerun/read_depth/breseq_01_cov_10.txt

module purge 
```