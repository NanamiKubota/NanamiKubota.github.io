---
title: "gbk to csv"
layout: single
permalink: /tutorials/gbk_to_csv
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2023-06-17
#classes: wide
---

# Converting .gbk to .csv

We will be working with a Genbank file (.gbk) so make sure you have that ready with you. If you want the same test file that I will be working with, you can download the file for *Pseudomonas aeruginosa* PA14 at [Pseudomonas.com](https://www.pseudomonas.com/strain/show/109) and clicking "GBK" under **Download Gene Annotations**, or by clicking [here](https://www.pseudomonas.com/downloads/pseudomonas/pgd_r_20_2/Pseudomonas_aeruginosa_UCBPP-PA14_109/Pseudomonas_aeruginosa_UCBPP-PA14_109.gbk.gz) (you'll get a pop up asking you where you want to save the file).

<br>

## Downloading gbk-to-csv converter

Once you have your gbk file, we will need to first convert it to csv. Technically, there are R packages that can read gbk files directly but they tend to be slow (and last time I tried it, it crashed my RStudio) so we're going to bypass this method by doing this on beagle and running my custom python script that converts gbk to csv (extract_gbk_to_csv.py).  

If you don't have it, you can download it through my Google Drive link [here](https://drive.google.com/file/d/1VbpH-wE4rxd0uu-FffSZoyYkEHTif01x/view?usp=sharing).  

Upload extract_gbk_to_csv.py, to your desired location in beagle. The filepath below reflects where I have the python script saved on my computer so this filepath will be different for everyone:  

```shell
scp -r /Users/kubotan/Documents/PMI/Cooper\ Lab/CS\ tutorial/script/extract_gbk_to_csv.py nak177@beagle.mmg.pitt.edu://home/nak177/scripts
```

<br>

I've saved the python script onto beagle in my home directory under the *scripts* folder.  

Once that is uploaded, you'll also want to upload your gbk file onto beagle if you haven't already.  

<mark>IMPORTANT: Your gbk file should only contain one chromosome or one plasmid. Some sequence files may contain multiple chromosomes and plasmids, in which case you will need to isolate into one in your gbk file.</mark>

<br>

## Run python script

Make sure you load miniconda3 before running the script:  

```shell
module load miniconda/miniconda-3
```

<br>

Now you can run the gbk-to-csv converter by doing:  

```shell
python3 /home/nak177/scripts/extract_gbk_to_csv.py -i /home/nak177/ref_seq/Pseudomonas_aeruginosa_UCBPP-PA14_109.gbk -o /home/nak177/ref_seq/PA14_gbk_to_csv
```

<br>

There are three file paths listed in the above line of code:  

1. Your python script location
2. -i followed by your filepath to your gbk file
3. -o followed by your output filepath with the prefix PA14_gbk_to_csv

<br> 

This will create a csv file named "PA14_gbk_to_csv.csv" within my ref_seq folder in my home directory on beagle.  

The arguments for the gbk-to-csv converter are as follows:  

- **-i** (or **--input**): filepath to your gbk file (required)
- **-o** (or **--output**): filepath + filename of your csv file. If output is not assigned, then it defaults to "gbk_to_csv.csv" which will be saved to your current directory.
