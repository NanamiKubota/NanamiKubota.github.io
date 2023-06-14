---
title: "Creating a virtual environment"
layout: single
permalink: /tutorials/virtual_environment
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2022-12-16
#classes: wide
---

<br>

> Note: This is a tutorial was made for the purposes of running on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

<br>

# What is a virtual environment and why you might want one

Think of a virtual environment as a separate box from beagle's main conda environment. This separate box is a clean slate that you can install any python version that you may need, and it doesn't come with any packages installed. While this may sound intimidating at first, this is a great place to install packages with dependencies that may conflict with conda packages that are already installed on beagle--including python.  

You may have noticed that when you load miniconda3 on beagle that the python version is at 3.6:
```bash
module load miniconda3 #check full file name later
python -V #V stands for version; equivalent of --version
```

<br>

See image below of what the output looks like:  

![](/images/beagle_python.png)


This might be problematic if the package that you want to use (like DefenseFinder and Bakta) require a newer python version. Not only will you run the risk that the package will fail to run, you might also accidentally autoupdate beagle's python version and autoupdate other conda packages on beagle upon installation which may break other packages that require the older versions to run.

To avoid this headache, creating a virtual environment is the safest way to install your newer python version and your package without worrying about conflicts in package versions.

***

<br>

# Set up a conda virtual environment on beagle

## Create the virtual environment

Before making a virtual environment, I like to make a folder in my home directory dedicated to the conda package that I am setting up the virtual environment for. To do so, run the following code but make sure to replace my home directory name with your own:

```bash
mkdir /home/nak177/your_conda_package_name
```

To set up a conda virtual environment, you will need python so load beagle's miniconda3:

```bash
module load miniconda
```

Make sure that miniconda3 (and not miniconda2) is loaded by using the following code:

```bash
module list
```

Most conda packages use python3 now, and miniconda3 uses python3 whereas miniconda2 loads python2.

Now that miniconda3 is loaded, we can then create a virtual environment by using python3. To create a virtual environment in your home directory run:

```python
conda create --prefix /home/nak177/your_conda_package_name/your_conda_package_name_env
```

This will create an environment named your_conda_package_name_env within the /home/nak177/your_conda_package_name/ folder.

## Activating and deactivating the virtual environment

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

## Installing conda packages

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
