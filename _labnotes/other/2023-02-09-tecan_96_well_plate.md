---
title:  "tecan 96 well plate conversion"
date: 2023-07-05
categories:
# tags:
#     - breseq
#     - gdtools
#     - bioinformatics
#     - script
layout: single_center_labnotes
excerpt: Convert tecan data output to column format
---

<div class="notice--info">
  <b>Objective:</b> convert tecan output from 96-well plate format to column format for downstream analysis. 
  <ul>
    <li>Take 96-well plate format, create a 3D array by stacking 2D dataframe, then convert back to 2D column format.</li>
  </ul>
</div>

<div class="notice--success">
  <b>Results:</b> <br>
  Successfully made script for 48h and 24h, however, modify script in the future to allow more flexible time points.
</div>

***

**2023-02-09**

Task:
- Make script for 48h growth curves.

***

**2023-07-05**

Task:
- Make script for 24h growth curves.