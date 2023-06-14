---
title:  "MPAO1 breseq and roary"
date: 2023-06-13
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center
excerpt: breseq MPAO1 strains from Secor lab and translate to PAO1 locus tags using roary
---

Objective: to whole genome sequence MPAO1 strains from the Secor lab and identify if potential concerning mutations exist. Use roary to translate MPAO1 locus tags into PAO1 locus tags.
- Pf6 deletion mutants have different colony size so look for potential variant calls that may explain this.
- 

Link to helpful roary tutorial:
https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/Notebooks/ROARY/ROARY.pdf

Use gff3 files generated from breseq run (found in /data/reference.gff3) and put it in one directory (/home/nak177/roary/gff/)

Then run:
```bash
module load roary/roary-3.12.0
cd /home/nak177/roary/gff/
roary -f output *.gff3
```

This creates a directory called "output" in your current directory. The "gene_presence_absence.csv" should contain the translation of locus tags between different strains.