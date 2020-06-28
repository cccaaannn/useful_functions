import pandas as pd
import numpy as np


# documentation
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html


# create dataframe from dict
data_dict = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=data_dict)

# create dataframe from numpy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
colum_names = ['a', 'b', 'c']
indexes = ["d", "e", "f"]
df = pd.DataFrame(arr, columns=colum_names)
df2 = pd.DataFrame(arr, columns=colum_names, index=indexes)



# select columns
df3 = df["a"]
df3 = df[["a","b"]]

# select rows with index int (iloc)
df3 = df.iloc[0]
df3 = df.iloc[[0]]
df3 = df.iloc[1:3, 0:3]

# select row by index name (loc)
df3 = df2.loc[["e", "f"]]


# select item by index int (iat)
value = df.iat[1, 2]

# select item by index and column name (at)
value = df.at[1, 'b']
value = df2.at["e", 'b']


# load csv
df = pd.read_csv("data_science-visualization/example_Data/train.csv", index_col=0)



# other
df2.index # get row name
df2.columns # get column names
df.shape # get size
df.copy() # deep copy df
df.describe()
df.head()
df.info()





