import pandas as pd
from pivottablejs import pivot_ui

df = pd.read_csv("data/placholder.csv")
pivot_ui(df)
