import numpy as np

result = np.array([10,15,30,45,60])

result = np.arange(5,15)

result = np.arange(50,101,5)

result = np.zeros(10)

result = np.ones(10)

result = np.linspace(0,100,5)

result = np.random.randint(10,30,5)

result = np.random.randn(10)

# result = np.random.randint(10,50,15).reshape(3,5)

matris = np.random.randint(10,50,15).reshape(3,5)

rowtotal = matris.sum(axis= 1)
coltotal = matris.sum(axis=0)
print("*"*50)
print(rowtotal)
print(coltotal)
print("*"*50)

result = matris.max()
result = matris.min()
result = matris.mean()

result = matris.argmax()
result = matris.argmin()

arr = np.arange(10,20)
result = arr[0:3]

result = arr[::-1]

result = matris[0]

result = matris[1,3]

result = matris[:,0]

result = matris**2

result = matris[matris % 2 == 0]



print(matris)
print(result)
 
