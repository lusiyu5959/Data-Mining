import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')  # 使用 TkAgg 后端
import matplotlib.pyplot as plt


file_path = "Mobiles Dataset (2025).csv"
df = pd.read_csv(file_path, encoding="latin1")

price_columns = [
    "Launched Price (Pakistan)",
    "Launched Price (India)",
    "Launched Price (China)",
    "Launched Price (USA)",
    "Launched Price (Dubai)"
]

def clean_price_data(price):
    if isinstance(price, str) and price.strip():
        try:
            return float("".join([c for c in price if c.isdigit() or c == "."]))
        except ValueError:
            return np.nan
    return np.nan if pd.isnull(price) else price

for col in price_columns:
    df[col] = df[col].apply(clean_price_data)

region_avg_prices = df.groupby("Launched Year")[price_columns].mean()

baseline_year = region_avg_prices.index.min()
normalized_prices = region_avg_prices / region_avg_prices.loc[baseline_year]

plt.figure(figsize=(18, 8))
sns.set(style="whitegrid")

normalized_prices.plot(kind="area", stacked=True, alpha=0.7, colormap="tab10")

plt.title("Smartphone Affordability Comparison Across Regions (Normalized Price Trend)")
plt.xlabel("Year")
plt.ylabel("Relative Price Trend (Baseline = 1)")
plt.legend(title="Region", loc="upper left")
plt.grid(True)

plt.show()
