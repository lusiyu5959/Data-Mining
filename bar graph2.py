import matplotlib.pyplot as plt
import pandas as pd
#Read the data in the data set
df = pd.read_csv(r'D:\Pycharm\CS422-数据挖掘\Mobiles Dataset (2025).csv', encoding='ISO-8859-1')
#Data cleaning
def clean_price(price):
    if isinstance(price, str):
        clean_str = ''.join(filter(lambda x: x.isdigit() or x == '.', price))
        try:
            return float(clean_str)
        except ValueError:
            return price
    return price
df['Launched Price (USA)'] = df['Launched Price (USA)'].apply(clean_price)
average_price = df.groupby('Launched Year')['Launched Price (USA)'].mean()#Group mean
#Year of treatment
Launched_Year = ['20' + str(year) if len(str(year)) == 2 else str(year) for year in average_price.index]
#Draw a bar chart
plt.figure(figsize=(8, 6))
plt.bar(Launched_Year, average_price)
plt.xticks(rotation=90)
#Add titles and labels
plt.title('Average Launched Price in USA by Year')
plt.xlabel('Year')
plt.ylabel('Average Launched Price (USA)')
plt.show()