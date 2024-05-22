import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]

numbers2 = np.array([[0,5,10],[15,20,25],[85,50,75]])

result = numbers2[1,1]
result = numbers2[:,2]

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1

arr2=arr1.copy()

arr1[0] = 20

print(arr1)
print(arr2)