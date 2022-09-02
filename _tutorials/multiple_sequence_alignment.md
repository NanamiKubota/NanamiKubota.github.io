---
title: "Graph multiple sequence alignment"
layout: single
permalink: /tutorials/multiple_sequence_alignment
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2022-08-22
#classes: wide
---

<br>

This tutorial will cover how to graph multiple sequence alignments on R. I used to use the msa package on R, but the package is no longer compatible with the new Apple M1 because Bioconductor is not compatible with the M1 version of R (i.e. arm64 version). To circumvent this, I will use multiple softwares including Geneious Prime to get our multiple sequence alignments. Alternatively, you can switch to the intel version of R and use Rosetta in order to use the msa package but we will not go over that in this tutorial.

<br>

# FASTA file preparation (Geneious)

I am interested in the *pf5r* gene in *Pseudomonas aeruginosa* PA14. I have compiled a fasta-style text file with the amino acid sequence of *pf5r* as well as genes from other *P. aeruginosa* strains that produced a hit when I blasted the gene against the Pseudomonas Genome Database. You can see a sample of my fasta file by clicking (here)["sample_data/ortholog_pf5r.fasta"] (clicking the hyperlink will prompt a download).

After you have your fasta file, import it into Geneious by clicking on the *Add* button and selecting *New Sequence...* as seen below: 

![](/images/geneious_add.png){: .image-resize .image-center}

Once your fasta file is imported, we will align the sequences. To do so, go to *Align/Assemble* and select *Multiple Align...* from the dropdown menu as seen below:

![](/images/geneious_multiple_align.png.png){: .image-resize .image-center}

Then choose your desired alignment algorithm. If you are unsure which one to use, [see this Geneious article which goes over each algorithm.]("https://help.geneious.com/hc/en-us/articles/360044627712-Which-multiple-alignment-algorithm-should-I-use-")

![](/images/geneious_alignment.png){: .image-resize .image-center}

After you choose an algorithm, Geneious should output an alignment for all of your sequences. Lets export this by clicking *Export* and selecting *Export Documents...* from the dropdown menu:

![](/images/geneious_export.png){: .image-resize .image-center}

For the export file format, choose *FASTA sequences/alignment*:

![](/images/geneious_export_format.png){: .image-resize .image-center}

Then select the file location to save the data to. After you have done this, Geneious will ask you about *Potential Data Loss*. Click *proceed* for this:

![](/images/geneious_data_loss.png){: .image-resize .image-center}

Then it will ask you about *FASTA sequences/alignment Export*. Make sure to select *Replace spaces in sequence name with underscores* and *Export missing ends of alignment as: gaps(-)* as seen below:

![](/images/geneious_alignment_fasta_export.png){: .image-resize .image-center}

Your fasta file should look something like [this](../sample_data/ortholog_pf5r_alignment.fasta) (click the hyperlink to download multiple alignment fasta file output).

<br>
# Visualize multiple alignment using ggmsa (R)

Open RStudio and install the [ggmsa package](http://yulab-smu.top/ggmsa/).

You can download the package by doing:
```R
if (!requireNamespace("devtools", quietly=TRUE))
    install.packages("devtools")
devtools::install_github("YuLab-SMU/ggmsa")
```

Once downloaded, load the ggmsa and ggplot2 package:
```R
library(ggmsa)
library(ggplot2)
```

Denote the filepath of your multiple sequence alignment fasta into the *fasta_filepath* variable:
```R
fasta_filepath <- "/Users/kubotan/Downloads/ortholog_pf5r alignment.fasta"
```
*Note your filepath will be different from mine.

Then once you have done that, you can plot your multiple sequence alignment by:
```R
ggmsa(fasta_filepath, color = "Chemistry_AA", font = "DroidSansMono", char_width = 0.5, seq_name = TRUE, show.legend = TRUE)
```

Your plot should look something like this:
![](/images/ortholog_pf5r_alignment.png)

The colors are based on the side-chain chemistry but a lot of the figure can be customized to fit your needs.

Read the [ggmsa documentation](http://yulab-smu.top/ggmsa/) to further understand how to color and customize your multiple sequence alignment plot.

You can save your plot by doing assigning your ggmsa function as a variable and using the ggsave function to save your picture:
```R
p <- ggmsa(fasta_filepath, color = "Chemistry_AA", font = "DroidSansMono", char_width = 0.5, seq_name = TRUE, show.legend = TRUE)
ggsave(plot=p, "/Users/kubotan/Documents/PMI/Cooper Lab/Prophage/sequences/data/pf repressor comparison/ortholog_pf5r_mutant_alignment.png", height = 7, width = 25, bg="white")
```

If you would like to select a sequence to become a reference sequence for all your other sequences to align to, you can do this by using the following parameters:
```R
ggmsa(fasta_filepath, color = "Chemistry_AA", font = "DroidSansMono", char_width = 0.5, seq_name = TRUE, ref = "Pseudomonas_aeruginosa_UCBPP-PA14", consensus_views = TRUE, disagreement = FALSE, use_dot = FALSE)
```

I picked the "Pseudomonas_aeruginosa_UCBPP-PA14" sequence to be my reference in this example.

Then your figure should look like this:
![](/images/ortholog_pf5r_alignment_consensus.png)