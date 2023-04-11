import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path


path = Path()

if not path.joinpath('data_2').exists():
    print('data_2 does not exist! let\'s create it...')
    Path(path.joinpath('data_2')).mkdir()
else:
    print('data_2 is already there...')

df = pd.read_excel('results.xlsx')
penguins = sns.load_dataset("penguins")
sns.histplot(data=df, x = df.Torsion, bins= 24)
# plt.show()


with open('penta-Si.gcd', 'r') as f:
    entries = [x.strip() for x in f.readlines()]  

