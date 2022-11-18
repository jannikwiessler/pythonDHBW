import pandas as pd

pd.set_option('display.max_columns',10 )

df = pd.read_csv("supermarket_sales.csv")
print(df.columns)
#print(df.groupby("City").mean())

newdf = df.loc[df["City"]=="Mandalay"]
print(newdf)