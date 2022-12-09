import pandas as pd
import matplotlib.pyplot as plt



pd.set_option('display.max_columns', 10)

# read the data
df = pd.read_csv("weatherHistory.csv")
#print(df.describe())

df = df[["Formatted Date", "Apparent Temperature (C)", "Humidity", "Wind Speed (km/h)"]]

df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df =df.set_index('Formatted Date')

df = df[['Apparent Temperature (C)','Humidity','Wind Speed (km/h)']].resample('MS').mean()
print(df.head(10))

plt.figure(figsize=(15,3))
plt.plot(df['Humidity'], label = 'Humidity', color ='blue',linestyle='dashed')
plt.plot(df['Apparent Temperature (C)'], label = 'Apparent temp.', color  = 'orange')
plt.title('Variation of Apparent temperature v/s Humidity', fontsize = 25)
plt.legend(loc=0, fontsize =12)
plt.xticks(fontsize = 15)
plt.yticks(fontsize=13)
plt.show()


plt.figure(figsize=(15,3))
plt.plot(df['Wind Speed (km/h)'], label = 'Wind Speed (km/h)', color ='red',linestyle='dotted')
plt.plot(df['Apparent Temperature (C)'], label = 'Apparent temp.', color  = 'orange')
plt.title('Variation of Apparent temperature v/s Wind Speed (km/h)', fontsize = 25)
plt.legend(loc=0, fontsize =12)
plt.xticks(fontsize = 15)
plt.yticks(fontsize=13)
plt.show()
