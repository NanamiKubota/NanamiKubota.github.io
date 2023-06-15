---
title:  "MPAO1 breseq and roary"
date: 2023-06-13
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: breseq MPAO1 strains from Secor lab and translate to PAO1 locus tags using roary
---

<div class="notice--info">
  <b>Objective:</b> to whole genome sequence MPAO1 strains from the Secor lab and identify if potential concerning mutations exist. Use roary to translate MPAO1 locus tags into PAO1 locus tags. 
  <ul>
    <li>Pf6 deletion mutants have different colony size so look for potential variant calls that may explain this.</li>
  </ul>
</div>

Link to helpful roary tutorial:
[https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/Notebooks/ROARY/ROARY.pdf](https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/Notebooks/ROARY/ROARY.pdf)

Roary uses gff files **with sequence information**. Make sure that gff files contain the sequence information as not all gff files do.

Luckily, gff3 files generated from breseq run (found in /data/reference.gff3) contain sequence information so this can be used. Put the gff3 files in one directory (/home/nak177/roary/gff/)

Then run:
```bash
module load roary/roary-3.12.0
cd /home/nak177/roary/gff/
roary -f output *.gff3
```

This creates a directory called "output" in your current directory. The "gene_presence_absence.csv" should contain the translation of locus tags between different strains.