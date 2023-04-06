import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel('results.xlsx')
penguins = sns.load_dataset("penguins")
sns.histplot(data=df, x = df.Torsion, bins= 24)
plt.show()