---
title:  "Pf repressor colony competition"
date: 2023-06-30
categories:
layout: single_center_labnotes
excerpt: Convert tiff files to gif/mp4 from colony competitions
hidden: false
---

To convert tiff files to jpeg:
```bash
for f in *.tiff; do echo "Converting $f"; convert -quality 90 "$f" jpg/"$(basename "$f" .tiff).jpg"; done
```

To convert jpg to gif:
```bash
ffmpeg \
  -framerate 10 \
  -pattern_type glob \
  -i '*.jpg' \
  out.gif \
```

To preview mp4
```bash
ffplay -vf eq=brightness=0.4:contrast=1.5 movie.mp4
```

To convert brightness (need to crop so that pixel numbers are even):
```bash
ffmpeg -framerate 10 -pattern_type glob -i '*.jpg' -vcodec libx264 \
-vf "crop=floor(iw/2)*2:floor(ih/2)*2,eq=brightness=0.4:contrast=1.5" \
-pix_fmt yuv420p movie.mp4
```

To just convert to mp4 without changing brightness and contrast:
```bash
ffmpeg -framerate 10 -pattern_type glob -i '*.jpg' -vcodec libx264 \
-vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" \
-pix_fmt yuv420p movie.mp4
```