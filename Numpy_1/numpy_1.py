import numpy as np

print(np.array([5,75,85,74]))

my_list = ["bucak","zeliha","tolunay",15,True,96.65]

print(f"listenin ilk tipi {type(my_list)}")

my_arr = np.array(my_list)

print(f"listenin son tipi {type(my_arr)}")

print(my_list)
print("*"*50)
print(my_arr)

print("*"*50)

print(np.random.rand(5,3))
print("*"*50)

print(np.random.randint(5,100,(5,3)))
print("*"*50)

print(np.random.uniform(-3,10,(5,3)))

print("*"*50)

print(np.random.randint(10,100,(4,4)))

my_Arry6 = np.random.randint(10,100,(4,4))
print(my_Arry6.shape)

print(my_Arry6.size)

print(my_Arry6.ndim)

my_arr1 = np.random.randint(1,20,(2,2))
my_arr1 = my_arr1*3

print(my_arr1)
print("*"*50)

my_arr2 = np.random.randint(1,20,(2,2))
my_arr2 = my_arr2*3
print(my_arr2)
print("*"*50)

print(my_arr1)
print(my_arr2)
print(my_arr1-my_arr2)
print("*"*50)



