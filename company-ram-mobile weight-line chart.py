import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

df=pd.read_csv(r'D:\dataset\Mobiles Dataset (2025).csv', encoding='cp1252')#Read data from the database based on the storage address
#Set the function to keep only the numerical part of all data, remove the units, and then perform subsequent calculations
def only_number(x):
    if isinstance(x, str):
        num_str=''.join([c for c in x if c.isdigit()])
        if num_str:
            return float(num_str)
    return x
#Read the RAM column and mobile weight column from the database, and apply the function to only read a portion of the data
df['RAM']=df['RAM'].apply(only_number)
df['Mobile Weight']=df['Mobile Weight'].apply(only_number)
#Grouping based on company name, due to the large amount of data, select the average value
ram=df.groupby('Company Name')['RAM'].mean()
weight=df.groupby('Company Name')['Mobile Weight'].mean()
#Draw the chart
mpl.rcParams['font.family'] = 'Arial'#Set the font of the final chart to 'Arial'
plt.rcParams['figure.dpi']=300#Set Resolution
mpl.rcParams['font.size']=8
plt.figure(figsize=(16, 6))
x=range(len(ram.index))#X-axis coordinate index
#Draw the line chart
plt.plot(x,ram.values,marker='o',color='blue',label='Average RAM Size')#RAM
plt.plot(x,weight.values,marker='s',color='red',label='Average Mobile Weight')#Weight
plt.title('Average RAM Size and Mobile Weight')#title
plt.xticks(x,ram.index,fontsize=4)
plt.xlabel('Company Name')
plt.ylabel('Values')
#Add data labels
for i,v in enumerate(ram.values):
    plt.annotate(f'{v:.2f}',(i, v),textcoords='offset points',xytext=(0, 5),ha='center',fontsize=4)
for i,v in enumerate(weight.values):
    plt.annotate(f'{v:.2f}',(i, v),textcoords='offset points',xytext=(0, 5),ha='center',fontsize=4)
#Explicit Line Chart
plt.legend()
plt.show()
