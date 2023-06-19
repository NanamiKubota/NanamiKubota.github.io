---
title:  "MPAO1 breseq and Roary"
date: 2023-06-13
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: breseq MPAO1 strains and translate to PAO1 locus tags using Roary
---

<div class="notice--info">
  <b>Objective:</b> to whole genome sequence MPAO1 strains from the Secor lab and identify if potential concerning mutations exist. Use Roary to translate MPAO1 locus tags into PAO1 locus tags. 
  <ul>
    <li>Pf6 deletion mutants have different colony size so look for potential variant calls that may explain this.</li>
  </ul>
</div>

<div class="notice--success">
  <b>Results:</b> 
  <ul>
    <li>Pf6 deletion mutants have mutations between xisF4 and pf4r, making them a possible Pf repressor mutant.</li>
    <li>Created rough pipeline from breseq gdtool parser output to Roary</li>
  </ul>
</div>

Link to helpful Roary tutorial:
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

***

**2023-06-14**

Tasks completed:
- create an R script that translates locus tags using Roary output

To do:
- modify it to include translations of gene product and JC calls

***

**2023-06-15**

Tasks completed:
- modified R script to translate JC calls and gene product
- Ran breseq again MPAO1 + Pf5 combined genome to check for Pf5 contamination
  - No contamination found


***

**2023-06-16**

- read depth mapping of MPAO1 sequencing data (breseq output) against MPAO1 Pf4 and Pf6 genome using gggenes (R script)
- translation table of MPAO1 Pf4 and Pf6 against PAO1 Pf4

