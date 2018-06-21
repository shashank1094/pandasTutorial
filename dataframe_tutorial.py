import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})
print("DATAFRAME IS :: \n", df)

# https://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing
# Different Choices for Indexing

# Normal Slicing
print("Normal", df[:2], sep="\n")
# But this doesn't work >>>print("Normal", df[0], sep="\n")

# Single row
print("Single Row", df.loc[0], type(df.loc[0]), sep="\n")

# Multiple Row
print("Multiple Row", df.loc[0:], type(df.loc[0:]), sep="\n")

# Single Column
print("Single Column", df["A"], type(df["A"]), sep="\n")
# Multiple Columns
print("Multiple Columns", df[["A", "B"]], type(df[["A", "B"]]), sep="\n")

# # Applying function on a cloumn in dataframe
# for c in df.columns:
#     if c == "B":
#         gg = df[c].apply(str.upper) # Function can be a lambda function
#         print(gg)

# # How to find if elements exist in dataframe / series
# print("COMPLETE DATAFRAME")
# print(df.isin([1, 3, 12, 'a']))
# print(df[df.isin([1, 3, 12, 'a'])])
# print(df[~df.isin([1, 3, 12, 'a'])])
#
# print("SINGLE COLUMN IN DATAFRAME/SERIES")
# print(df.A.isin([1, 3, 12, 'a']))
# print(df[df.A.isin([1, 3, 12, 'a'])])
# print(df[~df.A.isin([1, 3, 12, 'a'])])
