---
title: "Rosetta Strain: Multiple Sequence Align (MSA) Genbank / Reference Sequences"
layout: single
permalink: /tutorials/rosetta_strain
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2025-10-30
hidden: false
---

<br>

<div class="notice--warning">
  <b>This tutorial is only temporarily available.</b> I have made it visible for now but this page may go under construction again.
</div>

<br>

> Note: This is a tutorial was made for the purposes of running on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

<br>

# Why this tool might be useful

<br>

When using a newly assembled genome as a reference sequence in breseq, breseq may not pick up on any variants that were already present in the reference sequence. 

For example, if the isolate used to make the reference sequence already has a truncated efflux gene, you may be unaware of this truncation as breseq will only pick up on differences between the reference sequence and reads. If both reference and newly sequence reads share this truncation, breseq will not see a difference between the two and you will be blind to the fact that the isolates have a truncated efflux. 

Additionally, using this reference sequence with a truncated efflux to map reads from a population sample can lead to further issues. Any isolates that have the non-truncated efflux will have reads that do not map to the reference, as the reference will be missing part of the gene. Consequently, any variation in the truncated region will be undetectable.

As such, it is important to compare newly assembled genomes between each other and other lab and/or environmental strains. One way to do this is to align the genomes against each other and check for differences manually on software like Geneious. However, this method is tedious especially if you have multiple genomes and many loci to compare.

To address this, my msa_comparison tool can quickly compare multiple genomes across multiple loci, generating a table summarizing amino acid differences. The script also generates FASTA files of the multiple sequence alignment (MSA) for each locus. You can use these FASTA files to then visualize the alignment in R or other programs. To plot MSA in R, refer to my [multiple sequence alignment tutorial](/tutorials/multiple_sequence_alignment#visualize-multiple-alignment-using-ggmsa-r).

<br>

# Preparing your data and environment

<br>

## List of required files and information

<br>

**1 - Genbank files of all the genomes**: Before you run the msa_comparison tool, make sure you have Genbank files of all of your genomes either in .gbk or .gbff format. All files should have the same file extension (i.e. format) for the script to work. 

For this tutorial, I will use the Genbank files of different *Pseudomonas aeruginosa* strains from the [Pseudomonas Genome Database](https://pseudomonas.com/).

As an example, you can locate the same files that I used here (you will be redirected to the Pseudomonas Genome Database):
- [PAO1 (reference strain)](https://pseudomonas.com/strain/show?id=107)
- [PA14 (another well studied strain)](https://pseudomonas.com/strain/show?id=109)
- [SF416 (environmental strain)](https://pseudomonas.com/strain/show?id=23020)
- [D-2 (environmental strain)](https://pseudomonas.com/strain/show?id=17309)

To download the Genbank file, go under the "Download Gene Annotations" and click on "GBK" to start your download.

<br>

**2 - Roary output file**: You will also need to run Roary on all of the genomes that you plan to MSA. Refer to my [Roary tutorial](/tutorials/roary) for more information. You will need the *gene_presence_absence.csv* output that Roary generates.

I ran Roary on the four *P. aeruginosa* genomes, and you can [download the gene_presence_absence.csv file here](/sample_data/gene_presence_absence.csv) to quickly continue on the tutorial (click on the hyperlink to get a pop-up to start your download, or alternatively, visit [my GitHub page](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/sample_data/gene_presence_absence.csv)). Check out my [Roary tutorial](/tutorials/roary) for more information on Roary.

<br>

**3 - Name of reference genome**: The script will ask you to designate one of your genomes as the "reference". It will find all amino acid differences between this reference genome and the rest of your genomes and save it into a csv file. I usually pick a lab strain to do this comparison. The name should match your Genbank filename for the reference genome.

I will pick the PAO1 strain as my "reference" genome as an example.

<br>

**4 - Loci list**: a csv file that contains a list of loci that you want to MSA. Use the "reference" strain's locus tag.

Since I will be using PAO1 as the reference genome, my locus tags should be PAO1's locus tags. For this example, I will use ten different loci. The csv table should be structured like below:

| locus_tags |
|------------|
| PA1078     |
| PA2018     |
| PA2399     |
| PA5017     |
| PA0763     |
| PA1430     |
| PA4601     |
| PA4525     |
| PA3551     |
| PA5549     |

You can [download my example by clicking here](/sample_data/locus_list.csv) (clicking the hyperlink will prompt a popup).

<br>

## Load necessary files and modules onto beagle

<br>

> <mark><b>UPDATE: You do not need to make a virtual environment anymore as clustal omega and its dependencies have been globally installed onto beagle.</b></mark> Information on how to install clustal omega has moved to the section, [Misc (Download Clustal Omega and dependencies)](#misc-download-clustal-omega-and-dependencies), in case you want to install it locally onto your computer.

<br>

You can find my python script (msa_comparison.py) on my GitHub page [here](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/msa_comparison.py). 

Download this and upload it to beagle. If you don't know how to upload files from your local computer to beagle, refer to the [Basics in Command Line](/tutorials/basics_in_command_line) tutorial.

You should also upload your Genbank files, Roary output file, and locus list csv file to beagle if it isn't in your directory already.

Log into beagle.

We will need python 3 so load miniconda3:
```
module load miniconda/miniconda-3
```
<br>

Load clustal omega too:
```
module load clustal-omega/clustal-omega-1.2.4
```

<br>

# Run the msa_comparison script

<br>

These are the following arguments for the msa_comparison script:

- '-g', '--genbank': Location of your directory that contains the Genbank file (gbk or gbff) of each strain to be aligned. Required.
- '-f', '--format': format of the genbank input file (gbk or gbff). Optional. Defaults to gbk.
- '-r', '--roary': Path to your roary gene_presence_absence.csv output file. Required.
- '-ref', '--reference': Name of your reference strain which must match its respective column name in roary. Required.
- '-l', '--loci': Path to the csv file containing a list of loci to MSA. Required.
-  '-o', '--output': Path of the output file. Required.

<br>

Since I have all of my files in my home directory, the following filepaths will be for my use. Please change the filepaths to your own directory when you run the following code.

Then run msa_comparison.py via:
```
python3 /home/nak177/scripts/msa_comparison.py -g /home/nak177/msa_comparison_tutorial/ref_seq/ -r /home/nak177/msa_comparison_tutorial/roary/gene_presence_absence.csv -ref PAO1 -l /home/nak177/msa_comparison_tutorial/locus_list.csv -o /home/nak177/msa_comparison_tutorial/
```

<br>

If you're using gbff instead of gbk, you will need to indicate this using the -f or --format argument (the default it gbk):
```
python3 /home/nak177/scripts/msa_comparison.py -g /home/nak177/msa_comparison_tutorial/ref_seq/ -r /home/nak177/msa_comparison_tutorial/roary/gene_presence_absence.csv -ref PAO1 -l /home/nak177/msa_comparison_tutorial/locus_list.csv -o /home/nak177/msa_comparison_tutorial/ -f gbff
```

<br>

Again, you might need to replace the file paths in the above line of code to the filepaths of where your files and directories are located.

Running the above code should produce the following:
- alignment directory that contains fasta files of your MSA. You can [use these files to plot MSA in R](/tutorials/multiple_sequence_alignment).
- output_data.csv which will contain information in your different strains relative to your reference strain. Amino acids are denoted with their respective one letter code, unless there is a deletion or unaligned amino acid in which case a dash (-) is used to denote the mismatch.
  - First column (AA_Position): denotes the amino acid position where the difference is found
  - Second column (Ref_AA): the amino acid in your reference sequence
  - Third column (Ref_locus): the locus tag in your reference sequence
  - Fourth column (Strain_AA): the amino acid in your other strain(s)
  - Fifth column (Strain_ID): the name of your strain where the amino acid change is found

<br>

<br>

***
***

<b><mark>Ignore the section below unless you would like to know how to install clustal omega locally on your computer</mark></b>

***
***

<br>

# Misc (Download Clustal Omega and dependencies)

<br>

> Note: This is not necessary on beagle as I have installed Clustal Omega and argtable globally on beagle. However, I will leave this section available in case anyone needs to install packages locally.

<br>

Make sure the virtual environment is activated from here on out.

You will need to download Clustal Omega. To do so, first download the source code (this will download the file to your current working directory):
```
wget http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz
```

<br>

Then unzip the source code (this will unzip the file in the current working directory):
```
tar -xf clustal-omega-1.2.4.tar.gz
```

<br>

Clustal Omega requires argtable to run so we will also download that:
```
wget http://prdownloads.sourceforge.net/argtable/argtable2-13.tar.gz
```

<br>

Unzip argtable too:
```
tar -xf argtable2-13.tar.gz
```

<br>

To compile and install argtable, we will change directory (cd) into argtable2-13 and run the following code (Note: your prefix will be different from my path. In my case, I am using the directory that I downloaded all my files into):
```
cd argtable2-13
./configure --prefix=/home/nak177/msa_comparison_tutorial/
make
make check
make install
make clean
```

<br>

Change directory and move out of the argtable2-13 directory. In my case, I will return to the following directory:
```
cd /home/nak177/msa_comparison_tutorial/
```

<br>

Change directory into the Clustal Omega directory. The install information for Clustal Omega is found in the "INSTALL" file. In short, you can run the following to install:
```
cd clustal-omega-1.2.4/
./configure --prefix=/home/nak177/msa_comparison_tutorial/ CFLAGS="-I/home/nak177/ms
a_comparison_tutorial/include" LDFLAGS="-L/home/nak177/msa_comparison_tutorial/lib"
make
make install
```

<br>

Make sure that you *don't* get the following error in your console:
```
configure: error: Could not find argtable2.h. Try $ ./configure CFLAGS='-Iyour-argtable2-include-path
```

<br>

For me, this installs clustalo into the bin directory (i.e. /home/nak177/msa_comparison_tutorial/bin/). Now, we must add this bin path into PATH:
```
PATH=$PATH:/home/nak177/msa_comparison_tutorial/bin/
```

<br>

This allows beagle to find clustalo. Check that clustalo is properly called by running the following (it should output the version number):
```
clustalo --version
```

<br>

If you don't see an output of the version number into the console, then something went wrong. Please carefully review that all the filepaths were entered correctly.

<br>