# https://stackoverflow.com/questions/50959624/iterate-over-different-dataframe#50959706

import pandas as pd

names = ["Mike", "Dani", "Scott", "Josh", "Nate", "Sandy"]
ids = [1, 2, 3, 4, 5, 6]
master = pd.DataFrame({"ID": ids, "Name": names})
# print(master)

names_second = ["Mike", "Dani", "Scott", "Sandy"]
ids_second = [1, 2, 3, 6]
second = pd.DataFrame({"ID": ids_second, "Name": names_second})
# print(second)

names_third = ["Mike", "Dani", "Scott", "Josh", "Nate"]
ids_third = [1, 2, 3, 4, 5]
third = pd.DataFrame({"ID": ids_third, "Name": names_third})
# print(third)

cmp_master_second, cmp_master_third = master[~master.ID.isin(second.ID)], master[~master.ID.isin(third.ID)]
print(cmp_master_second)
print('\n-------- Seperate dataframes -----------\n')
print(cmp_master_third)
