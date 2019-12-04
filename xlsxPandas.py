import pandas as pd

data = pd.read_csv("nba.csv", encoding="utf8")
for i, j in data.iterrows():
        print(j.to_string()) #this will remove the default dtype: object when printing each row value