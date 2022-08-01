---
title: "DefenseFinder"
layout: single
permalink: /tutorials/defense_finder
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2022-05-14
#classes: wide
---

<br>

> Note: This is a tutorial was made for the purposes of running on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

<br>

Source:  

The Nature publication on DefenseFinder by Tesson and colleagues can be found [here](https://doi.org/10.1038/s41467-022-30269-9).

<br>

# Setting up DefenseFinder

DefenseFinder recommends that the program is installed in a virtual environment. This is especially important for beagle since beagle's python version is 3.6.10 and we will need python version >=3.7 to run DefenseFinder.

However, updating beagle's python version can cause compatibility issues with other scripts, so we will install an updated version of python within the virtual environment.

## Create a virtual environment

We will need python so in beagle load miniconda by running:

```bash
module load miniconda
```

Make sure that miniconda3 (and not miniconda2) is loaded by using the following code:

```bash
module list
```

Miniconda3 uses python3 whereas miniconda2 loads python2. We will need python 3 for DefenseFinder.

Now that miniconda3 is loaded, we can then create a virtual environment by using python3. To create a virtual environment run:

```python
conda create --prefix /home/nak177/defense_finder/defensefinder_env
```

This will create an environment named defensefinder_env within the /home/nak177/defense_finder/ folder

## Activate virtual environment

To activate a virtual environment within beagle, we will need to run an extra line of code that is not needed if you are activating a virtual environment within your local computer (for example).

First run:

```python
source /opt/miniconda/miniconda3/etc/profile.d/conda.sh
```
Then activate your virtual environment by:

```python
conda activate /home/nak177/defense_finder/defensefinder_env
```
If you're only activating your virtual environment locally in your computer, you only need to run the conda activate code.

Congrats! You have created and activated your virtual environment! Now you can install the updated python version as well as other packages without affecting the rest of the beagle environment.

Don't deactivate your virtual environment just yet (since we need to install our programs), but if you need to deactivate a virtual environment, you can do this by running:

```python
conda deactivate
```

## Download python into virtual environment

**ABSOLUTELY MAKE SURE YOUR VIRTUAL ENVIRONMENT IS ACTIVATED BEFORE RUNNING THIS LINE OF CODE**

Otherwise you risk updating the python version for all of beagle which we don't want since that can break a lot of other dependent programs and scripts.

To install python 3.7 into your virtual environment, *activate your virtual environment first*, then:

```python
conda install python=3.7
```

Make sure to check your python version by running:

```python
python -V
```

Your output should look something like this:

![](/images/python_3.7.png)

Make sure you haven't accidentally updated the python version in beagle globally by deactivating your virtual environment and running:

```python
python -V
```

Your output should look like this:

![](/images/beagle_python.png)

## Install DefenseFinder and dependencies

Once you have successfully confirmed that python 3.7 was installed into your virtual environment, we will install DefenseFinder and its dependencies.

Follow the installation instruction on the GitHub page for DefenseFinder

# Convert output from tsv to csv

The output files for DefenseFinder are in tsv format. In order to be able to open the files in Excel, we will convert all three tsv output files into csv using the code below:

```python
import pandas as pd
import glob

#path to your folder containing the tsv files
path = '/Users/kubotan/Documents/PMI/Cooper Lab/Prophage/sequences/data/PAO1_defense_finder/'

#grab files with .tsv extension 
tsvfiles = glob.glob(path + "/*.tsv") 

#loop to convert all tsv files in folder into csv
for t in tsvfiles:
    tsv = pd.read_table(t, sep='\t')
    tsv.to_csv(t[:-4] + '.csv', index=False)
```

Make sure to change the filepath so that it points to the folder with your tsv files.
