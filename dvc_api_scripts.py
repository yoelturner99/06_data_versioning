import pandas as pd
import dvc.api

path=r'data\wine_original.csv'
# repo=r'C:\Users\yoelt\Documents\MSc_DSTI\DSTI\MLOps\06_data_versioning'
repo="https://github.com/yoelturner99/06_data_versioning.git"

data_url = dvc.api.get_url(
  path=path,
  repo=repo,
  rev="v1"
  )

data = pd.read_csv(data_url, sep=";")
print(data)