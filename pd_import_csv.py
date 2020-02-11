import pandas as pd
import numpy as np
df_excel = pd.read_excel("sampledata.xlsx",nrows =3,header=None)
head = df_excel.iloc[1:2,0:2]
head.rename(columns={0:'lot1',1:'lot2',}, inplace=True)
newdf = pd.DataFrame(np.repeat(head.values,3,axis=0))
newdf.rename(columns={0:'lot1',1:'lot2',}, inplace=True)

head = head.append(newdf,ignore_index=True)


# df = pd.read_csv("sampledatas.csv")
# df['names']



df_excel = pd.read_excel("sampledata.xlsx",skiprows=4,header=None)
df_excel.fillna(0)
val = df_excel.iloc[:,[0]]
val.rename(columns={0:'population'}, inplace=True)
# val.rename(index={0: "x", 1: "y", 2: "z"}, inplace=True)
address = val['population']
val['population1']=address
val.merge(head,left_index=True, right_index=True)



# h5 = df_excel["header5"]
# h5.fillna(0)
# df_excel.loc["ff"]


