import numpy as np
import pandas as pd
 
dictionary = {"isim" : ["ali","veli","ahmet","furkan","aslan"],
              "yas"  : [15,16,17,18,19],
              "maas" : [100,200,300,400,500]}

veri = pd.DataFrame(dictionary)
print(veri)

print("*"*10)

print(veri.head())

print(veri.columns)
print("*"*10)

print(veri.info())
print("*"*10)

print(veri.describe())
print("*"*10)

print(veri["yas"])
print("*"*10)

veri["sehir"]=["ankara","istanbul","eskişehir","adana","diyarbkir"]
print(veri)
print("*"*10)

print(veri.loc[:,"yas"])
print("*"*10)

print(veri.loc[:3,"yas"])

print("*"*10)

print(veri.loc[:3,"yas":"sehir"])
print("*"*10)
print(veri.loc[:2,["yas","sehir"]])
print("*"*10)


dictionary = {"isim" : ["ali","veli","ahmet","furkan","aslan"],
              "yas"  : [15,16,17,18,19],
              "sehir":["izmir","ankara","konya","ankara","antalya"]}

veri = pd.DataFrame(dictionary)
print(veri)
print("*"*10)

filter1 = veri.yas > 16
print(filter1)

print("*"*10)

filter_veri = veri[filter1]
print(filter_veri)
print("*"*10)

ortalama_yas = veri.yas.mean()
print(ortalama_yas)

print("*"*10)


veri["YAS_GRUBU"] = ["kücük"if ortalama_yas > i else "büyük" for i in veri.yas]
print(veri)
print("*"*10)
print("*"*10)

sözlük1 = {"isim" : ["murat","ayse","hilal"],
              "yas"  : [33,45,66],
              "sehir":["ankara","ankara","antalya"]}
veri1 = pd.DataFrame(sözlük1)
print(veri1)
print("*"*10)

sözlük2 = {"isim" : ["murat","ayse","hilal"],
              "yas"  : [33,45,66],
              "sehir":["ankara","ankara","antalya"]}
veri2 = pd.DataFrame(sözlük2)
print(veri2)
print("*"*10)

veri_dikey = pd.concat([veri1,veri2],axis=0)
print(veri_dikey)
print("*"*10)

veri_yatay = pd.concat([veri1,veri2],axis=1)
print(veri_yatay)
print("*"*10)


