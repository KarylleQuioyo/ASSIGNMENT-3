
import numpy as np

# Saving an array to a csv file
print('EXAMPLE 1')
data1 = np.array([[2, 0], [5, 7]])
np.savetxt('data1.csv', data1, delimiter=',')

# loading data from a csv file
array = np.loadtxt('data1.csv', delimiter=',')

print('Array: \n', array)

print()

print('EXAMPLE 2')
# saving an array to a binary file
data2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
np.save('data2.npy', data2)

# loading data from a binary file
array = np.load('data2.npy')

print('Array: \n', array)

print()

print('EXAMPLE 3')
# saving an array to a compressed file
a = np.array([[12, 6, 0], [3, 7, 1]])
b = np.array([[9, 1, 14], [6, 7, 3]])
c = np.array([[67, 42, 10], [44, 2, 15]])
np.savez('arrays.npz', arr1=a, arr2=b, arr3=c)

# loading data from a compressed file
arrays = np.load('arrays.npz')

arr1 = arrays['arr1']
arr2 = arrays['arr2']
arr3 = arrays['arr3']

print('Array 1: \n', arr1, '\nArray 2: \n', arr2, '\nArray 3: \n', arr3)
