---
title: "Roary"
layout: single
permalink: /tutorials/roary
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2023-06-18
#classes: wide
---

> Note: This tutorial was made for the purposes of running Roary the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

Other resources:
The GitHub repository for Roary can be found [here](https://github.com/sanger-pathogens/Roary).
- The official website for Roary can be found [here](http://sanger-pathogens.github.io/Roary/).
- The publication on Roary can be found [here](https://doi.org/10.1093/bioinformatics/btv421).
- Another Roary tutorial that I found very helpful is the
[Roary Pathogen Informatics Training](https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/Notebooks/ROARY/ROARY.pdf) by the Pathogen Informatics at Wellcome Sanger Institute.

<br>

***

<br>

# Prepare GFFs with sequence information

Roary uses gff files **with sequence information**. Make sure that gff files contain the sequence information as not all gff files do.

Luckily, gff3 files generated from breseq run (found in /data/reference.gff3) contain sequence information so this can be used. Put the gff3 files in one directory (/home/nak177/roary/gff/)

<br>

***

<br>

# Run Roary

Load the Roary module on beagle by:
```bash
module load roary/roary-3.12.0
```

<br>

Then change your directory to within the directory will the gff files:
```bash
cd /home/nak177/roary/gff/
```

<br>

Run roary:
```bash
roary -f output *.gff3
```

<br>

The wildcard (*) indicates to grab all gff files in my current directory with a gff3 file extension. Running this creates a directory called "output" in your current directory. The "gene_presence_absence.csv" should contain the translation of locus tags between different strains.

Note: if you also have miniconda loaded at the same time, you can run into an error when you use the wildcard (*). Make sure that you only have roary loaded when running it.