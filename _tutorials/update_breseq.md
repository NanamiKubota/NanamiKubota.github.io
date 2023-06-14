---
title: "Updating breseq globally"
layout: single
permalink: /tutorials/update_breseq
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2023-04-24
#classes: wide
---

<br>

> Note: This is a tutorial was made for the purposes of running on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

<br>

# Requirements

To do a global install breseq (i.e. to update breseq globally so that all beagle users have access to the new breseq version), you must first have sudo permission. To do so, consult Vaughn and ask JV to get sudo privileges.

Once you have sudo privileges, download the latest breseq version from the [breseq Github repository](https://github.com/barricklab/breseq/releases).

If there are multiple different files available under *Assets*, choose the once that says "Source code (tar.gz)", if available. Do not download the source package that says linux (even though beagle uses Linux). This is because we want the Makefile or configure script, and this script is needed to manually compile the package.

Upload the tar.gz file to your home directory:
```bash
scp -r /Users/kubotan/Downloads/breseq-0.38.1.tar.gz nak177@beagle.mmg.pitt.edu://home/nak177/
```

<br>

Don't unzip the file just yet. We will do this once we move the compressed file into the `/opt/breseq/` directory.

<br>

# Prepare install

Some of the breseq installation documentation is outdated (most likely written for breseq 0.37.0, which was when the doc was last updated) so the following steps were used to install 0.38.1.

> Note: Your mileage for the following steps may vary and highly depends on whether the updated version still follows the same installation format. These steps work for 0.38.1 but may need modification for newer versions.

Copy your compressed source package into the breseq folder that contains all the other versions (i.e., this is in */opt/breseq/*):
```bash
sudo cp /home/nak177/breseq-0.38.1.tar.gz /opt/breseq/
```

Make sure to change directory (cd) into */opt/breseq/* and then decompress the tar.gz file:
```bash
sudo tar -xf breseq-0.38.1.tar.gz
```

Change your current directory so that you are within the source code for the latest breseq version (in this case it is breseq 0.38.1)
```bash
cd breseq-0.38.1/
```


```bash
sudo autoreconf -i
```

```bash
sudo ./configure --prefix=/opt/breseq/
```

```bash
sudo make
```

```bash
sudo make test
```

```bash
sudo make install
```

# add to modulefiles

Check where the /act/modulefiles are for the previous breseq version:
```bash
module show breseq/breseq-0.35.0
```

We will need to create a new one so that the latest breseq is available when users `module load` breseq.

The easiest way to do this is to copy the old file and rename it as the latest version.

First change directory (cd) into the modulefiles directory for breseq:
```bash
cd /act/modulefiles/breseq/
```

Now copy the old version and rename it as the new version:
```bash
sudo cp breseq-0.35.0 breseq-0.38.1
```

The contents of the modulefile should look like this:
```
#%Module1.0

## modules breseq/breseq-0.35.0

## modulefiles/breseq/breseq-0.35.0.

proc ModulesHelp {} {

        global version modroot

        puts stderr "breseq/breseq-0.35.0 - sets the Environment to use breseq"

}

module-whatis   "Sets the environment to use breseq"


if { ![is-loaded gcc/gcc-4.9.4] } {
     module load gcc/gcc-4.9.4
}

if { ![is-loaded samtools/samtools-1.6] } {
     module load samtools/samtools-1.6
}

if { ![is-loaded r/r-3.2.1] } {
     module load r/r-3.2.1
}

if { ![is-loaded bowtie2/bowtie2-2.3.3] } {
     module load bowtie2/bowtie2-2.3.3
}

# Tcl use only

set     root    /opt/breseq/breseq-0.35.0
set     version 0.35.0
set     sys     linux86_64

prepend-path    PATH    $root/bin
prepend-path    LD_LIBRARY_PATH /usr/lib64
```

Now we will need to edit the contents of the modulefile for breseq-0.38.1 so that all instances of 0.35.0 says 0.38.1:
```bash
sudo -s
nano breseq-0.38.1
```

**MAKE SURE TO EXIT SUDO ROOT ONCE YOU ARE DONE WITH NANO:**
```bash
exit
```


# update breseq dependencies

You may need to update other packages that breseq depends on (such as bowtie and R).