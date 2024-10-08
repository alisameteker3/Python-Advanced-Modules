import numpy as np


dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)
print(type(dizi))
print(dizi.shape)

dizi2 = dizi.reshape(3,5)

print("*"*10)

print("şekil : ",dizi2.shape)
print("Boyut : ",dizi2.ndim)
print("Veri tipi : ", dizi.dtype)
print("Boy : ", dizi2.size)

print("*"*10)

dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)
print("*"*10)

sifir_dizi = np.zeros((3,4))
print(sifir_dizi)
print("*"*10)

birler_dizi = np.ones((3,5))
print(birler_dizi)
print("*"*10)

bos_array = np.empty((3,4))
print(bos_array)
print("*"*10)

dizi_aralik = np.arange(10,51,5)
print(dizi_aralik)
print("*"*10)

dizi_aralik2 = np.linspace(10,50,5)
print(dizi_aralik2)
print("*"*10)

a = np.random.randint(1,7,7)
b = np.random.randint(1,7,7)
print(a+b)
print("*"*10)

rasgele_dizi = np.random.random((3,3))
print(rasgele_dizi)
print("*"*10)

index_dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(index_dizi[5])

print(index_dizi[0:5])

print("*"*10)

