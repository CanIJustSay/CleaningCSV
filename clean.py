import pandas as pd

df = pd.read_csv("bothDatas.csv")
print(df.shape)

del df["sy_gaiamagerr2"]
del df["sy_gaiamagerr1"]
del df["sy_vmag"]
del df["sy_gaiamag"]
del df["sy_kmagerr2"]
del df["sy_kmagerr1"]
del df["sy_kmag"]
del df["sy_vmagerr2"]
del df["sy_vmagerr1"]
del df["sy_disterr2"]
del df["sy_dist"]
del df["dec"]
print(df.shape)

df.to_csv("cleanCSV.csv")