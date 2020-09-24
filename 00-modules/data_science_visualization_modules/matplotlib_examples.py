import numpy as np
import matplotlib.pyplot as plt


# documentation
# https://matplotlib.org/3.1.3/api/pyplot_summary.html


# scatter plot
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
plt.scatter(x, y, c='tab:blue', label='stuff')
plt.legend(loc=2)
# plt.show()


# line plot 
x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.plot(x, y, c='tab:green', label='aaa')
plt.plot(x, y, "-o", c='tab:green', label='aaa') # plot with dots
# plt.show()


# bar chart
x = np.arange(3)
plt.bar(x, height=[1,2,3])
plt.xticks(x, ['a','b','c'])
plt.ylabel('y')
plt.xlabel('x')
# plt.show()


# subplots (pie chart and histogram)
arr_pie = np.array([40,30,70])
arr_pie_labels = ["a","b","c"]

arr_hst = np.random.normal(size=1000)

fig1, axs = plt.subplots(2)
axs[0].pie(arr_pie, labels=arr_pie_labels)
axs[0].title.set_text("pie chart")

axs[1].hist(arr_hst, bins=30) 
axs[1].title.set_text("histogram")
# plt.show()



