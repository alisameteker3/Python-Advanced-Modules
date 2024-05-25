import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10
print("*"*50)
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)
print("*"*50)
result  = mnumbers1 >55

print(mnumbers1[result])

print(result)

