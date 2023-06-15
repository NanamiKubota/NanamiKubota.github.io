---
title:  "breseq gdtools commands"
date: 2023-06-06
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: gdtool commands for outputting variant call table
---

<div class="notice--info">
  <b>Objective:</b> Compile gdtool help resource for future reference. 
</div>

Notes from gdtools help:

> Usage: gdtools [COMMAND] [OPTIONS] Manipulate Genome Diff (*.gd) files using the following commands.
> 
> General:
> - VALIDATE - check formatting of input files
> - APPLY - apply mutations to a sequence
> - ANNOTATE (or COMPARE) - annotate the effects of mutations and compare multiple samples
> - MUTATIONS - (re)predict mutations from evidence
> - CHECK - compare control versus test mutations
> - NORMALIZE - normalize mutation positions and annotations
> 
> Set and Filtering Operations:
> - SUBTRACT - remove mutations in one file from another
> - INTERSECT - keep shared mutations in two files
> - UNION/MERGE - combine mutations, removing duplicates
> - FILTER/REMOVE - remove mutations matching specified conditions
> - MASK - remove mutation predictions in masked regions
> - NOT-EVIDENCE - remove evidence not used by any mutations
> 
> Format Conversions:
> - GD2VCF - GD to Variant Call Format (VCF)
> - VCF2GD - Variant Call Format(VCF) to GD
> - GD2GVF - GD to Genome Variation Format (GVF)
> - GD2CIRCOS - GD to Circos Data
> - MUMMER2MASK - Create a mask GD file from MUMmer output
> 
> Analysis:
> - COUNT - count statistics for different types of mutations
> - PHYLOGENY - create maximum parsimony tree from mutations (requires PHYLIP)
> 
> TACC Utilities:
> - DOWNLOAD - download reference and read files from GD header info
> - RUNFILE - create a commands file and launcher script for use on TACC

To subtract ancestor variant calls from mutant, use:

```bash
gdtools SUBTRACT -o output.gd mutant.gd ancestor.gd
```

The general input usage:
```bash
gdtools SUBTRACT [-o output.gd] input.gd subtract1.gd [subtract2.gd ...]
```

To annotate gd files as TSV:
```bash
gdtools ANNOTATE -e [-o annotated.tsv] -f TSV -r reference.gbk input.1.gd [input.2.gd ... ]
```

Don't use the html output (the default) because it will not show you missing coverage (MC) or junction (JC) calls.

The -e argument:
```bash
-e,--preserve-evidence           By default evidence items with two-letter codes are
                                   removed (RA, JC, MC, ...). Supply this option to retain
                                   them. Only affects output in GD and JSON formats. This
                                   option can only be used with a single input GD file
                                   (i.e., not in COMPARE mode). 
```

***

**2023-06-12**

Information of gdtools SUBTRACT function

```bash
gdtools SUBTRACT [-o output.gd] input.gd subtract1.gd [subtract2.gd ...]
  -h,--help                        Display detailed help message
  -o,--output <arg>                output GD file (DEFAULT=output.gd)
  -p,--phylogeny-aware             Check the optional 'phylogeny_id' field when deciding
                                   if entries are equivalent
  -f,--frequency-aware             Use the frequencies of mutations when performing the
                                   subtraction. Normally an input mutation is removed if
                                   it appears at any frequency in a subtracted file. In
                                   this mode its frequency is reduced by the frequency in
                                   each subtracted file. If the resulting frequency is
                                   zero or below, then the mutation is removed.
  -v,--verbose                     verbose mode

Creates a new Genome Diff file that contains all mutation entries that are still
present in the input file after removing mutations that are in any of the
subtracted Genome Diff files. All evidence and validation entries are
retained in the output file.
```

Info on GenomeDiff (gd) file:
https://barricklab.org/twiki/pub/Lab/ToolsBacterialGenomeResequencing/documentation/gd_format.html?highlight=letter
