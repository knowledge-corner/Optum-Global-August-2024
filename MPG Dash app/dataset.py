import pandas as pd
import numpy as np

df = pd.read_csv(r"auto-mpg.csv")
df.replace({"?" : 0}, inplace=True)
df.horsepower = df.horsepower.astype(int)
df.origin = df.origin.map({1 : "USA", 2 : "Germany", 3 : "Japan"})
print(df.head())
