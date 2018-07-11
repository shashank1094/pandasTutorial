import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
dates = pd.date_range('20180701', periods=6)
# print(dates, type(dates))
s.index = dates
print(s)
print(pd.show_versions())
