---
title: "Running breseq on beagle"
layout: single
permalink: /tutorials/breseq
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2021-03-06
#classes: wide
---

> Note: This is a tutorial was made for the purposes of running breseq on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

***

# Getting started

In order to access the Cooper Lab servers, you must have permission to access them. To do so, make sure to email JV to receive permission prior to getting started.

You will also need Pulse Secure installed into your computer. You can receive a free copy of Pulse Secure through Pitt by going to [software.pitt.edu](https://software.pitt.edu/). You will need you Pitt ID to log in and download the software. Make sure to also select the appropriate version for your computer.

After you install Pulse Secure, follow the PowerPoint from JV to set up Pulse Secure. The first password is your Pitt ID password and the second password is "*push*". This should send a push notification to your Duo app for your two-factor authentication. Make sure to save your settings to make connecting to the server easier in the future.

If you are having trouble, make sure to check [here](https://www.technology.pitt.edu/services/pittnet-vpn-pulse-secure) as Pitt has listed the requirements needed to connect through Pulse Secure as well as a step-by-step guide for different devices.

## Connect to beagle

We will be working with the server, Beagle, to run our breseq analysis.

To connect to the server, use *ssh* followed by your own Pitt username @beagle.mmg.pitt.edu. In my case, since my Pitt ID is nak177, my line of code will be:

```bash
ssh nak177@beagle.mmg.pitt.edu
```

The format should be *ssh yourPittID@<span>beagle.mmg.pitt.edu* . After you hit enter, you will be asked for your password. Type in your password and hit enter.

Your screen should look something like this:

![](/images/beagle_home_screen.png)

Now you are ready to use Beagle!

## Access sequence data

First check your working directory:

```bash
pwd 
```

This should tell you where you are located within Beagle. When you first connect to Beagle, you should be within your own home directory.

In my case, I am located at:

```bash
/home/nak177
```

Your working directory will be different from mine and will most likely be within your own directory.

Now we will access the directory which contains the burk+pa experiment that Chris Marshall did.

The data for the burk/pa experiments are found in Chris Marshall's directory. We can see this by entering:
```bash
ls /home/cwm47/burk_pa/chris_exp
```

When you get your reads back from a sequencing machine or company, you want to check the quality of your reads to make sure they are good enough to work with. It looks like the reads saved here are already trimmed. This means we can skip the step of "cleaning" the raw sequence reads. 

I will update this tutorial at a later date to include how to do quality control and trimming but for the purposes of this tutorial, we will skip this for now.

***

# Quality control

To be updated.

<br>

***

# Trim reads

To be updated.

<br>

***

# Run breseq

## Download reference sequences

Before we run breseq, we must first download our reference sequence for *Burkholderia cenocepacia* HI2424 from the [Burkholderia Genome Database](https://burkholderia.com/strain/show?id=130) and *Pseudomonas aeruginosa* PA14 from the [Pseudomonas Genome Database](https://pseudomonas.com/strain/show?id=109).

Download the gene annotation files by scrolling down to "Download Gene Annotations" and clicking on "GBK" (this means the file is in GenBank format).

After you have downloaded this files, lets move the files onto your home directory in the Beagle server.

Open a new terminal window so that you have a new window that is not connected to the Beagle server but to your local environment.

In my case, this means that the beginning of my line of code shows:
```bash
(base) kubotan@kubotan-M1 ~ % 
```
instead of 
```bash
[nak177@beagle ref_seq]$
```

This will be different for your own local environment. As long as it does not say @beagle, then you should be good.

First, lets check where your downloaded files are located. In my case, I downloaded my .gbk files in my Downloads folder so I can see them using the ls function within my Downloads folder:
```bash
ls /Users/kubotan/Downloads/*.gbk.gz
```

The wildcard (*) is used to indicate that I want to list all the files within my Downloads folder with any file name as long as it ends with .gbk.gz. The .gz just indicates that the file is zipped 

For Mac users, the easiest way to get your file path (i.e. the direction to a particular folder) is by going to Finder and right clicking on your folder, hold down the Options key, and select "Copy Downloads as Pathname".

![](/images/copy_pathname.png)

Then in your new terminal window, type in ls and paste in your file path by doing Cmd+v with "/*.gbk.gz" added at the end:

```bash
ls /Users/kubotan/Downloads/*gbk.gz
```
Check to make sure that the output shows your downloaded files only.

```bash
/Users/kubotan/Downloads/Burkholderia_cenocepacia_B1_130.gbk.gz
/Users/kubotan/Downloads/Pseudomonas_aeruginosa_UCBPP-PA14_109.gbk.gz
```

Now we will upload these files from your computer to your home directory. To do so, use the scp function with -r, and make sure to indicate the correct file path for both your local and server directory. In my case, this will be:

```bash
scp -r /Users/kubotan/Downloads/*.gbk.gz nak177@beagle.mmg.pitt.edu://home/nak177/ref_seq
```

Note that I am uploading these files to MY home directory (i.e. nak177) into my folder called "ref_seq". Make sure you change the above line of code so that it has YOUR directory file path on it. Otherwise, I will get your uploaded files into my directory.

It is good practice to keep your home directory organized. I recommend that you make a folder in your home directory where you will store your reference sequences. You can do this by doing:

```bash
mkdir ref_seq
```

After your files are uploaded, lets unzip them. First, make sure that you are in the directory where your files are located and then use the gzip function:

```bash
gzip -d *.gz
```

The wildcard (*) here indicates to unzip anything with the extension .gz in your working directory.

Check that your files are unzipped by doing:

```bash
ls
```

<br>

## Combine reference sequences

Now you should have .gbk files downloaded and unzipped. We will now need to combine these reference sequences into one big reference sequence.

To do this, first edit the python script combine_sequences.py in a text editor so that you change my directory to your own home directory. Then run the python script combine_sequences.py by:

```bash
python combine_sequences.py
```

This should create two files. One of them is burk_merged.gbk, which is just a merged files of all the Burkholderia content, since the Burkholderia .gbk contained 4 "chromosomes". See https://www.ncbi.nlm.nih.gov/assembly/GCA_000203955.1 for more info. I separated each "chromosome" by 50 N bases so that we can see where each start and end. We can ignore this particular file for now.

We are interested in the hi2424_pa14_2022.gbk file which contains both Burkholderia and PA14 genomes. I separated the Burkholderia and PA14 genome by 100 N bases. We will use this to run our breseq on the co-cultured sequences.

<br>

## Run breseq

We will be modifying Chris Marshall's script a little for our breseq run.

Take a look at cwm_burk_pa.sh (i.e. Chris's script) and burk_pa_breseq_2022.sh (my modified one) as reference.

Modify burk_pa_breseq_2022.sh in a text editor so that the computer will know where your files are located. Hint: replace any file path that has "nak177" in it with your own file path.

Additionally, there are #SBATCH at the top of the bash script. These are optional but I recommend having the first one in your bash script:
 - #SBATCH --job-name=your_job_name indicates what you want to name the job as once you send the bash script for computing (it is recommended that you name your job since everyone can see what jobs are running on the server)
 - #SBATCH --mail-user=your_email_address indicates where you would like to receive emails on updates on your job
 - #SBATCH --mail-type=ALL indicates that the server will mail you when your job starts and when it ends. This may be useful especially for jobs that can take a long time to run.


This is an example of the script I modified from Chris Marshall:
```bash
#!/bin/bash

#SBATCH --job-name=breseq
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL


#run breseq
module load breseq
for i in {01..24}; do time breseq -p -r /home/nak177/ref_seq/hi2424_pa14_2022.gbk /home/cwm47/burk_pa/chris_exp/trim/"$i"_forward_paired.fq.gz /home/cwm47/burk_pa/chris_exp/trim/"$i"_forward_unpaired.fq.gz /home/cwm47/burk_pa/chris_exp/trim/"$i"_reverse_paired.fq.gz /home/cwm47/burk_pa/chris_exp/trim/"$i"_reverse_unpaired.fq.gz -o /home/nak177/burk_pa/breseq_pop/breseq_"$i" -j 16; done 

#run parser to get all into one file
module load miniconda/miniconda-3
python3 /home/cwm47/build/gscripts/breseq_parser.py -d /home/nak177/burk_pa/breseq_pop/ -f csv -o /home/nak177/burk_pa/breseq_pop/burk_pa_bre_out

module purge
```

To upload your modified script from your local environment to the server, you can use scp:
```bash
scp -r /Users/kubotan/Downloads/burk_pa_breseq_2022.sh nak177@beagle.mmg.pitt.edu://home/nak177/burk_pa
```

Make sure to modify the file path of the above code to suit your needs.

Once your modified script is ready and uploaded to your home directory on Beagle, it is good practice to use tmux (i.e. a terminal multiplexer). Tmux is useful because it can keep your job running even if you disconnect from the server. This means that if you run a job within a tmux session, then you can log off from the server and do other tasks on your computer but your job will keep running in the server.

To make a new tmux session, do:
```bash
tmux new -s name
```

Where *name* is can be whatever you want to call your tmux session. In my case, I named mine breseq:
```bash
tmux new -s breseq
```

Once you have your tmux session active, you can run your script by doing:
```bash
sbatch /home/nak177/burk_pa/burk_pa_breseq_2022.sh
```
You can check if your job was successfully submitted by typing:
```bash
squeue
```

Congrats! You have now successfully ran your first breseq run!

Since there are a lot of sequences to go through, the breseq may take a while to run. While this is happening, I recommend preparing your breseq script for the sequenced Day 7 co-cultures.

The concept is the same. You will just need to modify the script so that you are using the right file path names for the mono cultures. You can see a list of the sequences at:
```bash
ls /home/cwm47/burk_pa/chris_exp/trim_d7/
```

Note that there are only 23 sequences here while the other folder has 24. This means that you will also need to modify the loop in the script and change the number from 24 to 23.

Also make sure to make a new file path for your Day 7 sequences so that you don't accidentally overwrite your Day 16 breseq run.

Once you are done with this, we will learn how to extract the old locus tags for Burkholderia.