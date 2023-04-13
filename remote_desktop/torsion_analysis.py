from ccdc.io import EntryReader
from ccdc.search import QueryAtom, QueryBond
from ccdc.search import QuerySubstructure, ConnserSubstructure
from ccdc.search import SubstructureSearch

import pandas as pd

INFILE = r'C:\Users\csd\csds_data\scripts\penta-Si.cgd'
OUTPUT_FILENAME = 'results_SiO4C'

csd_reader = EntryReader('CSD')
# cgd_reader = EntryReader('penta-Si_short.gcd', format='identifiers')
# print(f'CSD database: {len(csd_reader)} entries')
# print(f'CGD file: {len(cgd_reader)} entries')


# substructure query for SiO4C
p = QuerySubstructure()
si = p.add_atom(QueryAtom('Si'))
si.num_bonds = 5
o1 = p.add_atom(QueryAtom('O'))
o2 = p.add_atom(QueryAtom('O'))
o3 = p.add_atom(QueryAtom('O'))
o4 = p.add_atom(QueryAtom('O'))
c = p.add_atom(QueryAtom('C'))
c1 = p.add_atom(QueryAtom('C'))
c2 = p.add_atom(QueryAtom('C'))
c3 = p.add_atom(QueryAtom('C'))
c4 = p.add_atom(QueryAtom('C'))
c.aromatic = True
c1.aromatic = True
c2.aromatic = True
c3.aromatic = True
c4.aromatic = True
_ = p.add_bond(QueryBond('Single'), si, o1)
_ = p.add_bond(QueryBond('Single'), si, o2)
_ = p.add_bond(QueryBond('Single'), si, o3)
_ = p.add_bond(QueryBond('Single'), si, o4)
_ = p.add_bond(QueryBond('Single'), si, c)
_ = p.add_bond(QueryBond('Single'), o1, c1)
_ = p.add_bond(QueryBond('Single'), o2, c2)
_ = p.add_bond(QueryBond('Single'), o3, c3)
_ = p.add_bond(QueryBond('Single'), o4, c4)

# A substructure can also be read in from a ConQuest Connser file.
# filepath = 'monochloropyridine.con'
filepath = 'pentaSi.con'
connser_substructure = ConnserSubstructure(filepath)

for qatom in p.atoms:  
    print('%d: %s' % (qatom.index, qatom))

# create search object
substructure_search = SubstructureSearch()
sub_id = substructure_search.add_substructure(p)

substructure_search.add_torsion_angle_measurement('TOR1',
    sub_id, 1,
    sub_id, 2,
    sub_id, 3,
    sub_id, 4)
substructure_search.add_torsion_angle_measurement('TOR2',
    sub_id, 6,
    sub_id, 7,
    sub_id, 8,
    sub_id, 9)
hits = substructure_search.search(csd_reader)

print('torsion O atoms:')

with open(f'{OUTPUT_FILENAME}.gcd', 'w') as f:
     for h in hits:
          f.writelines(f'{h.identifier}\n')
     
for h in hits:
        print('%8s %7.2f' % (h.identifier, h.measurements['TOR1']))

def write_torsion(hits):
    identifier, measurement_O, measurement_C = [], [], []
    for h in hits:
        identifier.append(h.identifier)
        measurement_O.append(h.measurements['TOR1'])
        measurement_C.append(h.measurements['TOR2'])
    df = pd.DataFrame({'identifier' : identifier,
                       'torsion_angle_O' : measurement_O,
                       'torsion_angle_C' : measurement_C})
    return df

df = write_torsion(hits)
df.to_excel(f'{OUTPUT_FILENAME}.xlsx')


print('torsion C atoms:')
for h in hits:
    print('%8s %7.2f' % (h.identifier, h.measurements['TOR2']))

hits_csd = substructure_search.search(csd_reader)
print(f'search whole CSD yields {len(hits_csd)} hits')
# hits_cgd = substructure_search.search(cgd_reader)
# print(f'search .cgd file yields {len(hits_cgd)} hits')






