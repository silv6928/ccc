# -*- coding: utf-8 -*-
"""
Tony Silva
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Anthony Silva/silvat/ccc/data/df.csv", sep=",", index_col=0)
df = df.sort_values(by=["timestamp"], ascending=[True])

print(df.head())

ans = df.loc[df.target==0,:]
abn = df.loc[df.target==1,:]

print(df.disposition_time.mean()/60)

# Call Time Stats
plt.figure()
df.loc[df.disposition_time < 30,:].disposition_time.hist()
plt.show()
plt.close()

plt.figure()
sns.countplot(x="target", data=df)
plt.show()
plt.close()

plt.figure()
sns.countplot(x="target", hue = "queued", data=df)
plt.show()
plt.close()
