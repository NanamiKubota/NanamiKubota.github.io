---
title: "Basics in gdtools"
layout: single
permalink: /tutorials/basics_in_gdtools
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2023-06-17
#classes: wide
---

> Note: This is a tutorial that uses breseq v0.38.1 and was made for lab members using the Cooper Lab's beagle server. Your mileage may vary depending on which breseq version you are using. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

Learn more about gdtools through the official breseq documentation:
  - [breseq documentation on gdtools](https://barricklab.org/twiki/pub/Lab/ToolsBacterialGenomeResequencing/documentation/gd_usage.html)

To learn more about GenomeDiff formats, the breseq documentation has a comprehensive explanation [here](https://barricklab.org/twiki/pub/Lab/ToolsBacterialGenomeResequencing/documentation/gd_format.html).

# Getting started

Load breseq version 0.38.1 on beagle:
```
module load breseq/breseq-0.38.1
```

Then run the following command to view the different commands and options for gdtools:
```
gdtools
```

> Note: If you run gdtools without first loading breseq v0.38.1, then you will get the old version of gdtools. We want the newer version as the older version is missing some newer functions.

Running just gdtools should give you the following output with information on commands and options that gdtools can do:
```
Usage: gdtools [COMMAND] [OPTIONS] Manipulate Genome Diff (*.gd) files using the following commands.

```


# SUBTRACT

The SUBTRACT command can be helpful if you want to remove the ancestor variant calls from your other samples. Note that it only removes variant calls that have three-letter codes (e.g. SNP, INS, DEL, etc.) and not two-letter codes (e.g. RA, JC, MC, etc.).

The general input usage for SUBTRACT is:
```bash
gdtools SUBTRACT [-o output.gd] input.gd subtract1.gd [subtract2.gd ...]
```

To subtract ancestor variant calls from mutant, use:
```bash
gdtools SUBTRACT -o output.gd mutant.gd ancestor.gd
```

# ANNOTATE

The ANNOTATE command can take .gd files and convert them into different file formats.

More information on ANNOTATE can be found on the [official breseeq documentation](https://barricklab.org/twiki/pub/Lab/ToolsBacterialGenomeResequencing/documentation/gd_usage.html).

I recomment not using the html output (the default) because it will not show you missing coverage (MC) or junction (JC) calls.

To annotate gd files as TSV:
```bash
gdtools ANNOTATE -e [-o annotated.tsv] -f TSV -r reference.gbk input.1.gd [input.2.gd ... ]
```

The -e (preserve-evidence) argument can be useful if you want to keep variant calls that are two-letter codes (RA, JC, and MC) and also variant calls that are flagged as marginal predictions. By default, ANNOTATE will not keep calls with the two-letter codes or marginal calls.

The -e argument:
```bash
-e,--preserve-evidence           By default evidence items with two-letter codes are
                                   removed (RA, JC, MC, ...). Supply this option to retain
                                   them. Only affects output in GD and JSON formats. This
                                   option can only be used with a single input GD file
                                   (i.e., not in COMPARE mode). 
```

The -r (reference) argument should point to where the reference file is located. The reference file can be in the following formats: GenBank, gff, FASTA.

The -o (output) argument should indicate the location and/or the filename of where the output should be saved to. The default is "annotated.gd".

The -f (format) argument indicates the file format of the output file. It defaults to html but you can also choose to convert to gd, tsv, phylip, or json. Again, I prefer to use the TSV format over the default html output as it will not show you missing coverage (MC) or junction (JC) calls.
