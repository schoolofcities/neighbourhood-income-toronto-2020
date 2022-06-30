import pandas as pd
import zipfile

zip2016 = "sc/98-401-X2016043_eng_CSV.zip"
file2016 = "98-401-X2016043_English_CSV_data.csv"

zf = zipfile.ZipFile(zip2016) 
df = pd.read_csv(zf.open(file2016), dtype = str, encoding='latin1')

# print(df["DIM: Profile of Census Tracts (2247)"])
# print(df["Member ID: Profile of Census Tracts (2247)"])
# print(df.tail(100))

df["Dim: Sex (3): Member ID: [1]: Total - Sex"] = df["Dim: Sex (3): Member ID: [1]: Total - Sex"].replace('x', None)
df["Dim: Sex (3): Member ID: [1]: Total - Sex"] = df["Dim: Sex (3): Member ID: [1]: Total - Sex"].replace('...', None)
df["Dim: Sex (3): Member ID: [1]: Total - Sex"] = df["Dim: Sex (3): Member ID: [1]: Total - Sex"].replace('..', None)
df["Dim: Sex (3): Member ID: [1]: Total - Sex"] = df["Dim: Sex (3): Member ID: [1]: Total - Sex"].replace('F', None)

df["Dim: Sex (3): Member ID: [1]: Total - Sex"] = df["Dim: Sex (3): Member ID: [1]: Total - Sex"].astype(float)
df["Member ID: Profile of Census Tracts (2247)"] = df["Member ID: Profile of Census Tracts (2247)"].astype(int)



variable_ids = [1,2,3,4,5,51,58,674,751,857,867]

df = df[df['Member ID: Profile of Census Tracts (2247)'].isin(variable_ids)]



df = df[["GEO_CODE (POR)","Member ID: Profile of Census Tracts (2247)","Dim: Sex (3): Member ID: [1]: Total - Sex"]]

df = pd.pivot(df, index="GEO_CODE (POR)", columns="Member ID: Profile of Census Tracts (2247)", values="Dim: Sex (3): Member ID: [1]: Total - Sex")

df.to_csv("clean2016.csv")
