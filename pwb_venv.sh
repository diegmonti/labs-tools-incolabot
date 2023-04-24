#!/bin/bash

# clean-up directories if they already exist
rm -fdr pwbvenv

# create a virtual environment
python3 -m venv pwbvenv

# activate it
source pwbvenv/bin/activate

# install dependencies
pip install --upgrade pip setuptools wheel
pip install pywikibot[mwoauth]
