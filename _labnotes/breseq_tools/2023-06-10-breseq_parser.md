---
title:  "breseq parser"
date: 2023-06-10
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: creating new breseq parser script from gdtools
---

<div class="notice--info">
  <b>Objective:</b> to create a better breseq parser that uses the breseq gdtool output rather than the html output to create a TSV file of variant calls.
</div>

Name of script: [breseq_parser_gdtools.py](/scripts/breseq_parser_gdtools.py)

***

**2023-06-10**

Tasks completed:
- grab file path of output.gd files in /data/ folder using glob function

```python
def getGDPaths(directory):
    for name in glob.glob(directory + '/**/data/output.gd', recursive=True):
        print(name)

if __name__ == "__main__":
    getGDPaths(args.directory)
```

***

**2023-06-11**

Tasks completed:
- run gdtools ANNOTATE on all output.gd files and output as TSV
- concatenate TSV files into one CSV file
- make bash script to run breseq_parser_gdtools.py script

**breseq parser completed**


***

**2023-06-12**

Potentially add functionality to remove ancestor mutations (with or without frequency parameter) before parsing data


***

**2023-06-13**

Tasks
- Added functionality to remove variant calls in ancestor from other strains. Does not support frequency subtraction which is a possible future implementation.
- Note: Output csv file contains all variant calls (including marginal calls and unknown base evidence (UN))
  - Created R script that filters marginal calls and UNs output
- Note: gdtool SUBTRACT still leaves two-letter variant calls (ex. JC, MC, RA) found in ancestor.
  - Hard to filter out JC and MC calls since they can have "fuzzy" ends
  - SUBTRACT does remove three-letter variant calls (ex. SNP, DEL, INS)