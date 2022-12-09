import pandas as pd

pd.set_option('display.max_columns', 10)

# read the data
df = pd.read_csv("supermarket_sales.csv")

# explore the data
print(df.columns)
print(df.head())

# count number of rows
print(df.count())
print(df["Invoice ID"].count())

# mean of all numerical columns
print(df["Total"].mean())

# count sales per supermaket branch (A,B,C)
print(df.groupby("Branch")["Invoice ID"].count())

# count sales records for gender in each supermarket branch
print(df.groupby(["Branch", "Gender"])["Invoice ID"].count())

# Filter for Supermaket A
print(df[df["Branch"] == "A"])

# number of sales records grouped by product line for each gener in supermaket B
print(df[df["Branch"] == "B"].groupby(["Product line", "Gender"])["Invoice ID"].count())

# write a function to generalize the supermaket and visualize the results
# write a function to visualize the mean sales price per product line and gender
