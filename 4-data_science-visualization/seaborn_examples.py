import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# documentation
# https://seaborn.pydata.org/


# scatter plot
df = sns.load_dataset("tips")  
sns.scatterplot(x='total_bill', y='tip', data=df)
# plt.show()


# line plot
df = pd.DataFrame(dict(time=np.arange(500),value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.fig.autofmt_xdate()
# plt.show()


# box plot
df = sns.load_dataset("planets")
sns.boxplot(x="distance", y="method", data=df, palette=sns.color_palette("Paired"))
# plt.show()


# colors
sns.palplot(sns.color_palette("Blues"))
sns.palplot(sns.light_palette("green"))
sns.palplot(sns.dark_palette("purple"))
sns.palplot(sns.color_palette("pastel"))
sns.palplot(sns.color_palette("Paired"))
# plt.show()

