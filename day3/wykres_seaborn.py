import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("orders_example.csv")

plt.figure(figsize=(8, 4))
sns.boxplot(y=df['score'], color="salmon")

plt.show()