

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])


arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])


arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])

print("1D Array:\n", arr1)
print("\n2D Array:\n", arr2)
print("\n3D Array:\n", arr3)


print("\nAddition:", arr1 + 10)
print("Multiplication:", arr1 * 2)
print("Element-wise square:", arr1 ** 2)

print("\nBroadcasting Example:")
print(arr2 + 10)  
print(arr2 + np.array([1, 2, 3])) 


print("\nStatistics on arr1:")
print("Mean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))
print("Sum:", np.sum(arr1))

py_list = [1, 2, 3, 4, 5]

print("\nPython List * 2:", py_list * 2)  
print("NumPy Array * 2:", arr1 * 2)      

print("Memory usage (NumPy):", arr1.nbytes, "bytes")




random_array = np.random.rand(3, 3)  
print("\nRandom Array:\n", random_array)




large_array = np.arange(1_000_000)
result = large_array * 2

print("\nVectorized calculation completed on 1,000,000 elements.")


print("\nArray Structure Info:")
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size (total elements):", arr2.size)
print("Data Type:", arr2.dtype)
