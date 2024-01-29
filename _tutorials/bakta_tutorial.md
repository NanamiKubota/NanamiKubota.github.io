---
title: "bakta tutorial"
layout: single
permalink: /tutorials/ref_manager
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2023-11-20
hidden: true
---

> Note: This is a tutorial was made for the purposes of running bakta on the Cooper Lab's beagle server. This is also still a working draft so please reach out if you get stuck or if anything is unclear.

***

# Create a bakta virtual environment

See tutorial on virtual environments to create a virtual environment. Then follow the instructions in the bakta GitHub repo https://github.com/oschwengers/bakta  to install.

Bakta version installed must be compatible with the bakta database version. For example, bakta v1.8 can work with database v5.0 but not with database v4.0. Likewise, bakta v1.6 works with database v4.0 but not v5.0.

## Bakta database
Note that the database is large (~30.83G for version 5.0) so make sure there is enough space before doing this.

# Update Database

The bakta database can be found here: https://zenodo.org/records/7669534

To update, do the following:
```bash
wget https://zenodo.org/record/7669534/files/db.tar.gz #change link as needed
tar -xzf db.tar.gz
rm db.tar.gz
amrfinder_update --force_update --database db/amrfinderplus-db/
```

