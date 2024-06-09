import pandas as pd
import numpy as np

personeller = {
    'Çalışan':['Amet yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali eker','Samet Eser','Orhan Ak'],
    'Departman':['İnsan Kaynakları','Bilgi işlem','Muhasebe','İnsan Kaynakları','AR-GE','Bilgi işlem','Data'],
    'Yaş':[30,25,45,50,23,34,42],
    'Semt':['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df
result = df['Maaş'].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

 
# for name,group in df.groupby("Semt"):
#     print(name)
#     print(group)

# for name,group in df.groupby("Departman"):
#     print(name)
#     print(group)


result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Bilgi işlem")

result = df.groupby("Departman")["Yaş"].mean()
result = df.groupby("Semt")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Yaş"].max()

result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]

result = df.groupby("Departman")[["Yaş","Maaş"]].agg(np.mean)
result = df.groupby("Departman")[["Yaş","Maaş"]].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]




print(result)
