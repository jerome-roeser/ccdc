import ccdc
from ccdc.search import QueryAtom
from ccdc.search import QueryBond
from ccdc.search import QuerySubstructure
from ccdc.search import SubstructureSearch
import pandas as pd


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
connser_substructure = ccdc.search.ConnserSubstructure(filepath)

for qatom in p.atoms:  
    print('%d: %s' % (qatom.index, qatom))


substructure_search = ccdc.search.SubstructureSearch()
sub_id = substructure_search.add_substructure(p)

print('torsion O atoms:')
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
hits = substructure_search.search()
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
df.to_excel('result_script.xlsx')


print('torsion C atoms:')
# substructure_search.add_torsion_angle_measurement('TOR2',
#     sub_id, 6,
#     sub_id, 7,
#     sub_id, 8,
#     sub_id, 9)
# hits = substructure_search.search()


for h in hits:
    print('%8s %7.2f' % (h.identifier, h.measurements['TOR2']))



