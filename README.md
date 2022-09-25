# Pandas Demo for IAC

Pandas demo for IAC...

## Getting Started

Repo contains...

## Details on Setting up Environment

Create new python virtual environment (below is in Terminal for Mac):
```
python3 -m venv path/folder_name
```

Activate new environment, install dependencies, set up kernel for Jypyter Notebook
```
source path/folder_name/bin/activate
```
Either install requirements.txt from repo (pip install -r requirements.txt) or individually:
```
pip install pandas numpy notebook ipykernel os
python3 -m ipykernel install --name folder_name --user
```
CD into folder for project, then run Jupyter Notebook
```
python3 -m notebook
```