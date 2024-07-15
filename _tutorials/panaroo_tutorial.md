
How to install locally for macOS (arm64)

Create a virtual environment that uses python v3.9

Use the following prompt if you have Homebrew:
```
/opt/homebrew/opt/python@3.9/bin/python3.9 -m venv panaroo_env
source panaroo_env/bin/activate
```

Check python version
```
python --version
```

Install dependencies (you need to download [MacPorts](https://www.macports.org/install.php) for cdhit and mafft):
```
sudo port install cdhit mafft
pip install biopython networkx gffutils joblib tdqm

# edlib needs to be older version
pip install edlib==1.3.8.post2

pip install git+https://github.com/gtonkinhill/panaroo
```

Check to see if panaroo was installed correctly
```
panaroo --version
```