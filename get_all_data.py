import pandas as pd
from pathlib import Path

df_current = pd.read_csv('usgs_current.csv')

path = Path("usgs_main.csv")

if path.is_file() == False:
  df_current.to_csv("usgs_main.csv", index = False)
else:
  # if the file already exists, save it to a dataframe and then append to a new one    
  df_main_old = pd.read_csv("usgs_main.csv")
  df_main_new = pd.concat([df_main_old,df_current])

  # deduplicate based on unique id
  df_main_new_drop_dupes = df_main_new.drop_duplicates(subset = "id", keep = "first")

  # save to dataframe and overwrite the old usgs_main file
  df_main_new_drop_dupes.to_csv("usgs_main.csv", index = False)

