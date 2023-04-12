import ccdc
from ccdc.search import QueryAtom
from ccdc.search import QueryBond
from ccdc.search import QuerySubstructure
from ccdc.search import SubstructureSearch


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
substructure_search.add_torsion_angle_measurement('TOR1',
    sub_id, 1,
    sub_id, 2,
    sub_id, 3,
    sub_id, 4)
hits = substructure_search.search()
for h in hits:
    print('%8s %7.2f' % (h.identifier, h.measurements['TOR1']))

substructure_search.add_torsion_angle_measurement('TOR1',
    sub_id, 5,
    sub_id, 6,
    sub_id, 7,
    sub_id, 8)
hits = substructure_search.search()
for h in hits:
    print('%8s %7.2f' % (h.identifier, h.measurements['TOR1']))
