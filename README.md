# Pandas Demo for IAC

A demo example of using Pandas!

## Getting Started

Data for this project is from [Kaggle](https://www.kaggle.com/)

Files included:
- Resources/SteamCharts.csv
  - Available at: [Popularity of Games on Steam](https://www.kaggle.com/michau96/popularity-of-games-on-steam/)
- pandas-demo-IAC
  - Jupyter Notebook example of Data Exploration (uses CSV file)
- pandas-demo-IAC
  - Jupyter Notebook example of Data Cleaning (uses JSON file - available at link below)
- Pandas for IAC.pptx
  - Short slide presentation explaining Pandas
- main.py
  - Short example of an ETL process using Pandas and sqlalchemy (local script)
  - Modifies as existing table in postgres
- transform_steps/cleaning.py
  - Example of possible cleaning steps in Pandas
  
Files not included:
- steam-reviews.json
  - Available at: [80000 Steam Games Dataset](https://www.kaggle.com/deepann/80000-steam-games-dataset/)

Schema used for postgres for main.py
- This must be set up in postgres first before running main.py file
[schema](schema.png "Schema")

## Quick Steps for Setting up Python Environment, Dependencies, and Jupyter Notebook

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
pip install pandas 
pip install numpy
pip install notebook
pip install ipykernel
python3 -m ipykernel install --name folder_name --user
```
CD into folder for project, then run Jupyter Notebook
```
python3 -m notebook
```
For main.py file:
```
pip install sqlalchemy
```

If running an M1 Chip for main.py file:
```
pip install psycopg2-binary
```