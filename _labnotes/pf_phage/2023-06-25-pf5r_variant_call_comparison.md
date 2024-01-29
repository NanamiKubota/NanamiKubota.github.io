---
title:  "pf5r variant call comparison"
date: 2023-06-25
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: Check to see if pf5r mutants have variant calls not in ancestor
---

<div class="notice--info">
  <b>Objective:</b> Compare pf5r mutant variant calls with ancestor
  <ul>
    <li>Check if there are variant calls present in pf5r mutants but not in ancestor</li>
    <li>Check if there are variant calls in ancestor but not in pf5r mutants</li>
  </ul>
  Pf5 pf5r phage mutant may select for cells with particular mutations. They may also select against cells with particular mutations.
</div>

Tasks:
- Filter through breseq output of pf5r mutants (G1, B1, 1306, and 1307) in R
- Make presence-absence matrix of variant calls by locus (or if between locus, by intergenic region)
- Find variant calls that are in all pf5r mutants but not in ancestor--or calls that are in ancestor but not in pf5r mutants

Results:
- No mutations (other than pf5r mutation) that may explain phenotype.