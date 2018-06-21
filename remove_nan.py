import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [[1, 2, 3, 4], [4, 5, 6, 7, 8], [7, 6, 4], np.nan, [1, 2]],
    'B': [[1, 2, 3, 4], [4, 5, 6, 7, 8], [3, 7, 9], np.nan, [4, 5]],
    'E': [np.nan, np.nan, np.nan, np.nan, np.nan],
    'F': [[2, 2], [4, 4], np.nan, [78, 90], np.nan]
})

# print(df)

# print(df.isnull())
df.applymap(lambda x: x if isinstance(x, list) else [])
print(df)
