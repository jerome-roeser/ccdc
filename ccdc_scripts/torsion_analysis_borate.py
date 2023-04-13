import ccdc
from ccdc.search import QueryAtom
from ccdc.search import QueryBond
from ccdc.search import QuerySubstructure
from ccdc.search import SubstructureSearch

import pandas as pd

OUTPUT_FILENAME = 'results_BO4'

# substructure query for BO4
p = QuerySubstructure()
b = p.add_atom(QueryAtom('B'))
b.num_bonds = 4
o1 = p.add_atom(QueryAtom('O'))
o2 = p.add_atom(QueryAtom('O'))
o3 = p.add_atom(QueryAtom('O'))
o4 = p.add_atom(QueryAtom('O'))
c1 = p.add_atom(QueryAtom('C'))
c2 = p.add_atom(QueryAtom('C'))
c3 = p.add_atom(QueryAtom('C'))
c4 = p.add_atom(QueryAtom('C'))
c1.aromatic = True
c2.aromatic = True
c3.aromatic = True
c4.aromatic = True
_ = p.add_bond(QueryBond('Single'), b, o1)
_ = p.add_bond(QueryBond('Single'), b, o2)
_ = p.add_bond(QueryBond('Single'), b, o3)
_ = p.add_bond(QueryBond('Single'), b, o4)
_ = p.add_bond(QueryBond('Single'), o1, c1)
_ = p.add_bond(QueryBond('Single'), o2, c2)
_ = p.add_bond(QueryBond('Aromatic'), c1, c2)
_ = p.add_bond(QueryBond('Single'), o3, c3)
_ = p.add_bond(QueryBond('Single'), o4, c4)
_ = p.add_bond(QueryBond('Aromatic'), c3, c4)

# A substructure can also be read in from a ConQuest Connser file.
# filepath = 'monochloropyridine.con'
filepath = 'pentaSi.con'
connser_substructure = ccdc.search.ConnserSubstructure(filepath)

for qatom in p.atoms:  
    print('%d: %s' % (qatom.index, qatom))


substructure_search = SubstructureSearch()
sub_id = substructure_search.add_substructure(p)

substructure_search.add_torsion_angle_measurement('TOR1',
    sub_id, 1,
    sub_id, 2,
    sub_id, 3,
    sub_id, 4)
substructure_search.add_torsion_angle_measurement('TOR2',
    sub_id, 5,
    sub_id, 6,
    sub_id, 7,
    sub_id, 8)
hits = substructure_search.search()

with open(f'{OUTPUT_FILENAME}.gcd', 'w') as f:
     for h in hits:
          f.writelines(f'{h.identifier}\n')

print('torsion O atoms:')
for h in hits:
    print('%8s %7.2f' % (h.identifier, h.measurements['TOR1']))

def write_torsion(hits):
    identifier, measurement_O, measurement_C = [], [], []
    a, b, c = [], [], []
    alpha, beta, gamma = [], [], []
    crystal_system, spacegroup = [], []
    cell_volume = []
    for h in hits:
        identifier.append(h.identifier)
        measurement_O.append(h.measurements['TOR1'])
        measurement_C.append(h.measurements['TOR2'])
        a.append(h.crystal.cell_lengths.a)
        b.append(h.crystal.cell_lengths.b)
        c.append(h.crystal.cell_lengths.c)
        alpha.append(h.crystal.cell_angles.alpha)
        beta.append(h.crystal.cell_angles.beta)
        gamma.append(h.crystal.cell_angles.gamma)
        crystal_system.append(h.crystal.crystal_system)
        spacegroup.append(h.crystal.spacegroup_symbol)
        cell_volume.append(h.crystal.cell_volume)
    df = pd.DataFrame({'identifier' : identifier,
                       'torsion_angle_O' : measurement_O,
                       'torsion_angle_C' : measurement_C,
                       'a':a,
                       'b':b,
                       'c':c,
                       'alpha':alpha,
                       'beta':beta,
                       'gamma':gamma,
                       'crystal_system':crystal_system,
                       'spacegroup':spacegroup,
                       'cell_volume':cell_volume
                       })
    return df

df = write_torsion(hits)
df.to_excel(f'{OUTPUT_FILENAME}.xlsx')

print('torsion C atoms:')
for h in hits:
    print('%8s %7.2f' % (h.identifier, h.measurements['TOR2']))
