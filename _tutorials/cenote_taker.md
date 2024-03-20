---
title: "Cenote-Taker 3 tutorial"
layout: single
permalink: /tutorials/cenote-taker
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2024-02-16
hidden: false
#classes: wide
---

> Note: This tutorial was made for the purposes of running Cenote-Taker 3 on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

The most recent version of Cenote-Taker as of writing this tutorial is Cenote-Taker 3. The official GitHub document for Cenote-Taker 3 can be found here: [https://github.com/mtisza1/Cenote-Taker3](https://github.com/mtisza1/Cenote-Taker3).

<br>

# Install Cenote-Taker 3

We will need to first load miniconda-3 before creating a virtual environment. To learn more on creating virtual environment, refer to my [conda virtual environment tutorial](/tutorials/virtual_environment).
```
module load miniconda/miniconda-3
source /opt/miniconda/miniconda3/etc/profile.d/conda.sh
```

<br>

Make sure to change the filepath to your directory when running the following code to create your virtual environment named "ct3_env":
```
conda create --prefix /home/nak177/cenote/cenote3/ct3_env -c conda-forge -c bioconda cenote-taker3
```

<br>

When asked, "Proceed ([y]/n)?" for installation of new packages, Type "y" for "yes".

Now activate your virtual environment:
```
conda activate ct3_env/
```

<br>

We will need to download the database and name the location "ct3_DBs". This may take more than an hour depending on the internet speed and stability:
```
get_ct3_dbs -o ct3_DBs --hmm T --mmseqs_tax T --mmseqs_cdd T --domain_list T --hhCDD T --hhPFAM T --hhPDB T
```

<br>

Then use the following code (making sure to change the filepath to match your path to your ct3_DBs):
```
conda env config vars set CENOTE_DBS=/home/nak177/cenote/cenote3/ct3_DBs
```

<br>

# Run Cenote-Taker 3

To be updated