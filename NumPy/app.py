# with as we can give a new name to the module and use that name to call it
import numpy as np

# np.array allow to create an array but if we check the type, is a numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(array.shape)  # shape will give us a tuple with the dimension of array/matrix

# initialize an array with zeros. We need to give a tuple to give the dimension
# by default np.zeros create an array with floating numbers
# using dtype=int we can specify we want integers
array2 = np.zeros((3, 4), dtype=int)
# ones does the same thing but fill it up with ones
array3 = np.ones((3, 4), dtype=int)
# full allow us to give the number to fill the matrix, in this case 5
array4 = np.full((3, 4), 5, dtype=int)
# random.random create a matrix filled with random floating numbers between 0 and 1. does not accept dtype
array5 = np.random.random((3, 4))
print(array2)
print(array3)
print(array4)
print(array5)

# an array can be accessed by index
print(array5[1, 3])
# with the followin expression we are able to test the values inside the matrix and get back a boolean value base on the condition
print(array5 > 0.2)
# here we use the same condition, but putting in inside the [] we request to print out a LIST of the values that satisfy the condintion
print(array5[array5 > 0.2])
# this return the sum of all the value in the array
print(np.sum(array5))
# in return a matrix with same dimension with the floor values
print(np.floor(array))  # we also have ceil and round that can be used

# we can execute basi math operation with numpy arrays
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)
print(first + 2)

inch = np.array([1, 2, 3])
cm = inch * 2.54
print(cm)
