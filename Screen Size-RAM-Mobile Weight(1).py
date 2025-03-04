import pandas as pd
import matplotlib.pyplot as plt

#Read files based on dataset addresses
df=pd.read_csv(r'D:/dataset/Mobiles Dataset (2025).csv',encoding='cp1252')
#Define a function to extract the numerical part
def all_number(x):
    if isinstance(x,str):
        #Extract the numerical part from the data (removing the influence of units)
        x=x.replace('inches','').replace(' ','')
        if ','in x:
            parts=[float(p)for p in x.split(',')if p.strip().replace('.', '', 1).isdigit()]
            #Determine empty data
            if parts:
                return sum(parts)/len(parts)
            else:
                return None
        num_str=''.join([c for c in x if c.isdigit() or c=='.'])
        if num_str:
            return float(num_str)
    return x
#Extract numbers from RAM column data
df['RAM']=df['RAM'].apply(all_number)
#Extract the numbers from the mobile weight column data
df['Mobile Weight']=df['Mobile Weight'].apply(all_number)
#Extract the numbers from the screen size column data
df['Screen Size']=df['Screen Size'].apply(all_number)
#After filtering out rows without data, group them by Screen Size and calculate the average RAM and Mobile Weight for each group
phone_group=df.dropna(subset=['Screen Size']).groupby('Screen Size')[['RAM', 'Mobile Weight']].mean().reset_index()
plt.rcParams['figure.dpi'] = 300#definition
plt.rcParams['font.sans-serif']=['WenQuanYi Zen Hei']#font
plt.figure(figsize=(10, 6))#Create Canvas
#Draw a scatter plot
plt.scatter(phone_group['Screen Size'],phone_group['RAM'], label='RAM', color='blue', alpha=0.5)
plt.scatter(phone_group['Screen Size'],phone_group['Mobile Weight'], label='Mobile Weight', color='red', alpha=0.5)
#Draw a scatter plot
plt.title('Screen Size,RAM,Mobile Weight')#title
plt.xlabel('Screen Size (inches)')#Draw the horizontal axis
plt.xticks()
plt.ylabel('Values')#Draw the vertical axis
#display graphics
plt.legend()
plt.show()
