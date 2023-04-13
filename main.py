import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path


path = Path()
sio4c = 'results_SiO4C.xlsx'
bo4 = 'results_BO4.xlsx'


def plot_torsion_histogramm_Si(file):
    df = pd.read_excel(file)
    df['abs_torsion_angle_O'] = df.torsion_angle_O.apply(lambda x: abs(x)-180 if abs(x) > 90 else abs(x))
    df['abs_torsion_angle_C'] = df.torsion_angle_C.apply(lambda x: abs(x)-180 if abs(x) > 90 else abs(x))

    # sns.histplot(data=df, x = df.abs_torsion_angle_O, bins= 24)
    sns.histplot(data=df, x = df.abs_torsion_angle_C, bins= 24)

def plot_torsion_histogramm_B(file):
    df = pd.read_excel(file)
    df['abs_torsion_angle_O'] = df.torsion_angle_O.apply(lambda x: abs(x)-180 if abs(x) < 0 else abs(x))
    df['abs_torsion_angle_C'] = df.torsion_angle_C.apply(lambda x: abs(x)-180 if abs(x) < 0 else abs(x))

    # sns.histplot(data=df, x = df.torsion_angle_O, bins= 24)
    # sns.histplot(data=df, x = df.torsion_angle_C, bins= 24)
    # sns.histplot(data=df, x = df.abs_torsion_angle_O, bins= 24)
    sns.histplot(data=df, x = df.abs_torsion_angle_C, bins= 24)

# plt.show()

plot_torsion_histogramm_Si(sio4c)
plot_torsion_histogramm_B(bo4)


# with open('penta-Si.gcd', 'r') as f:
#     entries = [x.strip() for x in f.readlines()]

