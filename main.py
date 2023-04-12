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
# penguins = sns.load_dataset("penguins")
# sns.histplot(data=df, x = df.Torsion, bins= 24)
# plt.show()

df_script = pd.read_excel('results_script.xlsx')
df_script['abs_torsion_O'] = df_script.torsion_O.apply(lambda x: abs(x)-180 if float(abs(x)) > 90 else abs(x))
df_script['abs_torsion_C'] = df_script.torsion_C.apply(lambda x: abs(x)-180 if float(abs(x)) > 90 else abs(x))

# sns.histplot(data=df_script, x = abs(df_script.torsion_O), bins= 24)
# sns.histplot(data=df_script, x = abs(df_script.torsion_C), bins= 24)
# sns.histplot(data=df_script, x = df_script.abs_torsion_O, bins= 24)
sns.histplot(data=df_script, x = df_script.abs_torsion_C, bins= 24)

df_script_non_aromaticC = pd.read_excel('results_script_non_aromaticC.xlsx')
df_script_non_aromaticC['abs_torsion_O'] = df_script_non_aromaticC.torsion_O.apply(lambda x: abs(x)-180 if float(abs(x)) > 90 else abs(x))
df_script_non_aromaticC['abs_torsion_C'] = df_script_non_aromaticC.torsion_C.apply(lambda x: abs(x)-180 if float(abs(x)) > 90 else abs(x))

# sns.histplot(data=df_script_non_aromaticC, x = abs(df_script_non_aromaticC.torsion_O), bins= 24)
# sns.histplot(data=df_script_non_aromaticC, x = abs(df_script_non_aromaticC.torsion_C), bins= 24)
# sns.histplot(data=df_script_non_aromaticC, x = df_script_non_aromaticC.abs_torsion_O, bins= 24)
# sns.histplot(data=df_script_non_aromaticC, x = df_script_non_aromaticC.abs_torsion_C, bins= 24)

df_script_B = pd.read_excel('results_script_B.xlsx')

# sns.histplot(data=df_script_B, x = df_script_B.torsion_O, bins= 24)


with open('penta-Si.gcd', 'r') as f:
    entries = [x.strip() for x in f.readlines()]

