# ARC-Demo
Demo for interacting with the [Abstraction and Reasoning Corpus (ARC)](https://github.com/fchollet/ARC).


# Setup

## Conda environment
```commandline
git clone --recurse-submodules https://github.com/RajK853/ARC-Demo.git
cd ARC-Demo
conda env create -f environment.yml
```

## Install Ipykernel for Jupyter Notebook
```commandline
conda activate demo-arc
python -m ipykernel install --user --name=demo-arc
```
