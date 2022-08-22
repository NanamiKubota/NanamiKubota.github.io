---
title: "Growth Curve"
layout: single
permalink: /tutorials/growth_curve
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2022-08-12
#classes: wide
---

<br>

This tutorial is for converting your plate reader data into growth curves in R. Since the Cooper lab has two different plate readers with difference version of the software, be sure to check which plate reader software you used before proceeding. I have divided the tutorial based on the old vs newer program.

The plate reader with the newer program is located by the centrifuge next to the chemical hood while the plate reader with the older program is located by the entrance.

# Load libraries and data files

## 96-well plate key

Make sure you make your own spreadsheet that tells you which well in your 96-well plate contained which samples. The general format of your spreadsheet should look like this, where the first column is your well and your second column is your sample name:

<table>
  <tr>
    <td class="tg-c3ow">A1</td>
    <td class="tg-c3ow">Strain1<br></td>
  </tr>
  <tr>
    <td class="tg-c3ow">A2</td>
    <td class="tg-c3ow">Strain1</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A3</td>
    <td class="tg-c3ow">Strain1</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A4</td>
    <td class="tg-c3ow">Strain2</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A5</td>
    <td class="tg-c3ow">Strain2</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A6</td>
    <td class="tg-c3ow">Strain2</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A7</td>
    <td class="tg-c3ow">Strain3</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A8</td>
    <td class="tg-c3ow">Strain3</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A9</td>
    <td class="tg-c3ow">Strain3</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A10</td>
    <td class="tg-c3ow">blank</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A11</td>
    <td class="tg-c3ow">blank</td>
  </tr>
  <tr>
    <td class="tg-c3ow">A12</td>
    <td class="tg-c3ow">blank</td>
  </tr>
  <tr>
    <td class="tg-c3ow">B1</td>
    <td class="tg-c3ow">Strain1</td>
  </tr>
  <tr>
    <td class="tg-c3ow">B2</td>
    <td class="tg-c3ow">Strain1</td>
  </tr>
  <tr>
    <td class="tg-c3ow">B3</td>
    <td class="tg-c3ow">Strain1</td>
  </tr>
  <tr>
    <td class="tg-c3ow">.<br>.<br>.</td>
    <td class="tg-c3ow">.<br>.<br>.</td>
  </tr>
  <tr>
    <td class="tg-c3ow">H12</td>
    <td class="tg-c3ow">blank</td>
  </tr>
</table>

You do not need a header, and you should denote your blank wells (i.e. your control wells that you will normalize to) as "blank" with a lowercase *b*. You should have 2 columns and a total of 96 rows in your spreadsheet that starts from A1 and ends with H12. Save this spreadsheet as a csv file. An example of this key spreadsheet can be found [here](/sample_data/Plate_key_sample.csv).

## Newer program

Make sure to have a csv file of your plate reader output. You can do this by first downloading the data as an Excel file, then clicking "Save as" to change it into a csv file. Check your file path of your csv file, as this will be different from mine:

```r
file <- "/Users/kubotan/Documents/PMI/Cooper Lab/Prophage/Plate reader/2022-06-08/2022-06-10 clinical isolates.csv" #filepath of your csv file
p <- read.csv(file,header=T,skip=2) #read the csv as a dataframe and skip the first row
```

If you inspect the dataframe, there are a few rows and column that we don't need (such as the last few rows and the temperature column, respectively). We will remove this:

```r
p <- head(p,-3) #remove last few rows
p <- p[,-2] #remove temperature column
```

***

## Older program

Export your data as a .txt file from the older program. Make sure to check your file path before reading the data file using the read.delim() function:

```r
file <- "/Users/kubotan/Documents/PMI/Cooper Lab/Prophage/Plate reader/2022-06-22/Data 06-24-22-111321.txt"
p <- read.delim(file,header=F,skip = 4)
```

We will need to clean the dataframe:
```r
pcol <- as.character(unlist(p[1,-c(2,99)])) #extract colname
p <- p[-c(1:3,101),-c(2,99)] #for 24 hr; use p[-c(1,195),-c(2,99)] for 48 hr
colnames(p) <- pcol
rownames(p) <- 1:97 #for 24 hr; use 1:193 for 48 hr
p[,2:97] <- sapply(p[,2:97],as.numeric) 
```

# Graph the growth curves

You will need the following libraries to graph the growth curves.

```r
library(ggplot2)
library(reshape2)
library(RColorBrewer)
```