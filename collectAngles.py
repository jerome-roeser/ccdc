import pandas as pd
from pathlib import Path



path = Path('data/')

da = pd.DataFrame()
for p in path.iterdir():
    if p.is_file():
        df = pd.read_csv(f'data/{p.name}')
        df['CCDC_code'] = p.name[:6]
        print(p.name)
        # df.Torsion.apply(pd.to_string, errors='coerce')
        # t = type(df.Torsion)
        da = pd.concat([da, df])

print(da)
# da.to_excel('results.xlsx')