import numpy as np


# documentation
# https://numpy.org/doc/1.18/reference/index.html


# load data
data = np.loadtxt("data_science-visualization/example_Data/data.txt")
data_str = np.loadtxt("data_science-visualization/example_Data/top50info.txt", dtype=np.str, delimiter='\t', skiprows=1)

# array
arr = np.array([2, 4, 6, 8, 10])

# arange
arr = np.arange(10)
arr = np.arange(2, 10)

# reshape
arr = np.arange(9).reshape((3, 3))

# random
arr = np.random.rand(10)
arr = np.random.randint(5, size=(5))
arr = np.random.randint(5, size=(2, 4))
arr = np.random.permutation(10)
arr = np.random.normal(size=10) # normal distribution
np.random.shuffle(arr)
np.random.seed(42)

# where
arr = np.array([1,1,3,
                2,1,2,
                2,2,3]).reshape((3, 3))
indexes = np.where(arr==3)
arr = arr[np.where(arr==3)[0]] # colum location


# select colum
arr = np.array([1,1,3,
                2,1,2,
                2,2,3]).reshape((3, 3))
arr = arr[:,0]

# select row
arr = np.array([1,1,3,
                2,1,2,
                2,2,3]).reshape((3, 3))
arr = arr[0,:]
arr = arr[0]


# sort
arr = np.random.rand(30).reshape((3, 10))
arr2 = np.sort(arr,axis=0) # sort all columns
arr2 = np.sort(arr,axis=1) # sort all rows

# sort by using ONLY first column and not change the order
arr2 = arr[arr[:,0].argsort()] 
# sort by using ONLY first row and not change the order
arr2 = arr[:,arr[0].argsort()] 

# argsort (sync sort 2 arrays)
arr = np.array([5, 3, 1, 2, 4])
arr2 = np.array(["e", "c", "a", "b", "d"])

sorted_indexes = arr.argsort()
arr = arr[sorted_indexes]
arr2 = arr2[sorted_indexes]


# concatenate
arr = np.arange(10)
arr2 = np.arange(10,20)

arr3 = np.concatenate((arr, arr2), axis=0)

arr = np.arange(10).reshape((5, 2))
arr2 = np.arange(10,20).reshape((5, 2))

arr3 = np.concatenate((arr, arr2), axis=None) # merge without dimension
arr3 = np.concatenate((arr, arr2), axis=0) # merge colum by colum
arr3 = np.concatenate((arr, arr2), axis=1) # merge row by row


