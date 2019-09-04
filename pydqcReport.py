import pandas as pd
from pydqc.data_compare import distribution_compare_pretty

train = pd.read_csv("data/placeholder.csv")
test = pd.read_csv("data/placholder2.csv")
distribution_compare_pretty(train, test, "SOME COLUMNS", figsize=None)
