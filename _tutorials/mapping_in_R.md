---
title: "Mapping in R"
layout: single
permalink: /tutorials/mapping_in_R
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2023-06-15
#classes: wide
---

> Note: This is the updated version and not the original script from 2020 as some of the R packages from the previous script are going to retire or be unsupported soon.

You will need the following packages:
```R
library(sf) 
library(ggplot2)
library(RColorBrewer)
library(plyr)
library(tibble)
library(grid)
```

<br>

Look up appropriate EPSG code for the region you want to map at https://epsg.io/  

We will be using EPSG:2263 as it encompasses New York Long Island.

To view information:
```R
st_crs("EPSG:2263")
```

<br>

Now get your map. I will use the 

Next we will read the wastewater sewershed/drainage area map and clean it: