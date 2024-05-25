

mylist= [95,52,15,45,40,50,89,65]


def filtreleme(deneme):
   bos_liste = []
   for i in deneme:
      if i < 50:
        bos_liste.append("kaldi")
      else:
        bos_liste.append("Gecti")
      return bos_liste

print(f"notlar = {mylist}")
print(f"not durumu = {filtreleme(mylist)}")