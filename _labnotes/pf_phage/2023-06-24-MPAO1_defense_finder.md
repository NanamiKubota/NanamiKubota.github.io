---
title:  "MPAO1 DefenseFinder"
date: 2023-06-13
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: Run DefenseFinder on MPAO1 and compare defense systems between Pa strains
---

<div class="notice--info">
  <b>Objective:</b> Run DefenseFinder on MPAO1 and see if defense systems is different between MPAO1, PAO1, and PA14. 
  <ul>
    <li>Previously have run DefenseFinder on PAO1 and PA14.</li>
    <li>Updated DefenseFiner model version to 1.2.2</li>
    <li>Maybe rerun PAO1 and PA14 again since models have been updated?</li>
        <ul>
            <li>yes, rerun as toxin-antitoxin in PAO1 & MPAO1 don't show up in PAO1 since it's an old run</li>
            <li>rerunning PAO1 still doesn't identify toxin-antitoxin in Pf4 while MPAO1 does show up</li>
        </ul>
    <li>Update DefenseFinder tutorial as it doesn't include script to run DefenseFinder</li>
  </ul>
</div>

GitHub page on DefenseFinder: [https://github.com/mdmparis/defense-finder](https://github.com/mdmparis/defense-finder)

***
**2023-06-24**

Tasks:
- Upload MPAO1 fasta protein (amino acid) sequence on beagle from Pseudomonas.com
- ran DefenseFinder on MPAO1 sequence
- compare defense systems between MPAO1, PAO1, and PA14
- check if variant calls in B1, G1, 1306, 1307, and ancestor is in a gene that may be involved in immunity
  - potential hit observed in all strains but it is in an intergenic region downstream of the gene so unlikely
  - other hits are most likely false positives (even if there are hmmer hits, might need full set of genes to be functional)

```bash
#!/usr/bin/bash

#SBATCH --job-name=deffind
#SBATCH -w node02
#SBATCH --mail-user=nak177@pitt.edu
#SBATCH --mail-type=ALL

module purge
module load hmmer/hmmer-3.2.1
module load miniconda/miniconda-3

source /opt/miniconda/miniconda3/etc/profile.d/conda.sh
conda activate /home/nak177/defense_finder/defensefinder_env

defense-finder run /home/nak177/ref_seq/Pseudomonas_aeruginosa_MPAO1_15934.faa -o /home/nak177/defense_finder/MPAO1/
defense-finder run /home/nak177/ref_seq/Pseudomonas_aeruginosa_PAO1_107.faa -o /home/nak177/defense_finder/PAO1_update/
defense-finder run /home/nak177/ref_seq/Pseudomonas_aeruginosa_UCBPP-PA14_109.faa -o /home/nak177/defense_finder/PA14_update/

module purge
```



***
**2023-06-26**

Tasks:
- Check for homologous antiviral systems between MPAO1, PA14, and PAO1
- Cross compare locus tags with Roary

Result
- No overlapping PA14 antiviral systems in MPAO1.