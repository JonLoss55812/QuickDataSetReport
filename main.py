import pandas as pd
import pandas_profiling

df = pd.read_csv("../data/plachholderdata.csv")
pandas_profiling.profileReport(df)\
  .to_file("../reports/placeholder.html")
