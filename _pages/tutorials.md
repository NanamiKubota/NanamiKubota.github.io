---
title: "Tutorials"
# layout: categories
permalink: /tutorials/
layout: single
toc: true
toc_sticky: true
toc_label: "Table of Contents"
author_profile: false
# classes: wide
collection: tutorial
---

This page contains a compilation of dry lab tutorials that I have written over the years. I am slowly integrating all of my tutorials onto the website so please let me know if you find an error anywhere. Hopefully by the end of this, I will have a directory that points to all my tutorials that may be useful to other lab members who need help with dry lab work.

The list of currently available tutorials are below (some tutorials may be under construction):

<br>

***

<br>

# Basics

> [Basics in R](/tutorials/basics_in_R): Goes over how to install R and RStudio, as well as some basic functions.

> [Basics in Command Line](/tutorials/basics_in_command_line): A cheat sheet for command line functions and terminal customization that may be useful.

> [Kaggle: Intro to machine learning](https://www.kaggle.com/learn/intro-to-machine-learning): Free course to get your hands wet in machine learning. Recommended to have at least some prior knowledge in python. Kaggle also have some free machine learning competitions (some with cash prizes) where you can test out your skills.

> See also the section for [Resources for learning a new programming language](#resources-for-learning-a-new-programming-language) 

<br>

***

<br>

# Graphs

>[Growth curves](/tutorials/growth_curve): Convert 96-well plate reader data to growth curves in R and calculate area under the curve, carrying capacity, and growth rate using the Growthcurver package.

>[Plot Geographical Data on a Map](/tutorials/mapping_in_R): Create maps in R to show geographical data (not to be confused with mapping in genomics!)

<br>


***

<br>

# Genomics

<br>

Tutorials on running analyses and graphing genomic data.

<br>

## Annotate

> [bakta](/tutorials/bakta): Under construction. Annotate bacterial genomes. To be updated.

> [Cenote-Taker3](/tutorials/cenote-taker): Still under construction. Identify and annotate virus genomes and genes. To be updated.

<br>

## breseq

> [Running breseq](/tutorials/breseq): Step-by-step tutorial on how to run breseq on the lab's beagle server.

> [breseq parser gdtools](/tutorials/breseq_parser_gdtools): Converting breseq outputs to CSV format to view on programs like Excel. Also goes over how to "translate" locus tags using Roary. Optional function to remove ancestor strain variant calls from other samples.

> [Basics in gdtools](/tutorials/basics_in_gdtools): Under construction. Use gdtools to manipulate and export breseq variant call data. To be updated.

> [Update breseq (need sudo privilege)](/tutorials/update_breseq/): Updating breseq version globally on beagle. Requires sudo privilege.

<br>

## Plot

> [gbk to genome map](/tutorials/gbk_to_genome_map): Convert GenBank files (.gbk files) to linear genome maps using the gggenes package in R.

>[Graph multiple sequence alignment](/tutorials/multiple_sequence_alignment): Take your FASTA sequence file and do multiple sequence alignment in Geneious before plotting it in R.

<br>

## Multiple Sequence Alignment (MSA)

>[Graph multiple sequence alignment](/tutorials/multiple_sequence_alignment): Take your FASTA sequence file and do multiple sequence alignment in Geneious before plotting it in R.

> [Multiple Sequence Align (MSA) Genbank / Reference Sequences](/tutorials/msa_gb_ref_seq): (Under construction) Multiple sequence alignment (MSA) Genbank files or your reference/alignment sequence across multiple loci and output a csv file that summarizes all of the amino acid changes.

<br>

## Roary

> [Roary](/tutorials/roary): Create a "Rosetta stone" (i.e. translation table) for locus tags of homologous genes across different strains. 

<br>

## Phage

> [DefenseFinder](/tutorials/defense_finder): Tool that finds antiviral systems in prokaryotic genomes.

> [Cenote-Taker3](/tutorials/cenote-taker): Still under construction. Identify and annotate virus genomes and genes. To be updated.

<br>

## Other

> [Convert .gbk (GenBank files) to .csv](/tutorials/gbk_to_csv): Take GenBank files and covert into csv file to view gene table on Excel or other programs.

> [Retrieving old locus tags](/tutorials/old_locus_tag): Extract old locus tags from GenBank files.

<br>

***

<br>

# Miscellaneous

> [Create a conda virtual environment](/tutorials/virtual_environment): Create a virtual environment in your beagle home directory to install packages that may have dependencies that conflict or are different version numbers than the ones on beagle.

> [Zotero-Obsidian reference manager pipeline](/404): Under construction. Link up Zotero and Obsidian to work together to cluster notes by topics rather than by paper. Includes templates for importing metadata from Zotero to Obsidian. Find relevant papers using ResearchRabbit. (My favorite way of finding papers and organizing my reference manager/notes.)

<br>

<hr style="height:5px;border:none;color:#B0B0B0;background-color:#B0B0B0;">

<br>

# Resources for learning a new programming language

Below are a list of websites that may be useful for learning a new programming language. 

> [freeCodeCamp](https://www.freecodecamp.org/): free, project-based learning module. I recommend their html and CSS course for those who want to knit R markdown to nice html files. Also a great foundation if you ever want to build a website on GitHub Pages. This is a concept-based approach rather than a language-based approach so it might be good if you are interested in learning terminology and new skills rather than learning a new coding language. Great for people who never took a formal computer science course like me, as it helps fill in some of the gaps in knowledge that you would otherwise cover if you took a course in computer science.

> [Exercism](https://exercism.org/): free and has over 60 different languages available. Good if you are looking to learn a new language like Python. However, I don't recommend the R tutorial for true beginners as it dives right into writing functions without much of an introduction. You might want to use Google as you complete each exercise, and this may help with your Googling skills (very important for writing code).

> [Codecademy](https://www.codecademy.com/): 7-day free trial for different learning modules. I recommend their "Learn the Command Line" course for Cooper Lab users who want to use beagle. Their "Learn Bash Scripting" is okay and goes over basic syntax but not as well-built as the command line tutorial. The modules is shorter though so if you have time during your free trial, go for it.
