import ccdc.search
#import ccdc.io
import os

from ccdc.io import EntryReader
from ccdc.io import MoleculeReader
from ccdc.conformer import GeometryAnalyser

from ccdc.search import QueryAtom
from ccdc.search import QueryBond
from ccdc.search import QuerySubstructure

# atom query for O atom, aromatic, cyclic
o = QueryAtom('O')
o.aromatic = True
o.cyclic = True
o.add_connected_element_count('Si', 1)

# substructure query for carbonyl
from ccdc.molecule import Bond
double_bond = Bond.BondType('Double')
substructure_query = QuerySubstructure()
query_atom1 = substructure_query.add_atom('C')
query_atom2 = substructure_query.add_atom('O')
query_bond = substructure_query.add_bond(double_bond, query_atom1, query_atom2)

# substructure query for COOH
s = QuerySubstructure()
c = s.add_atom(QueryAtom('C'))
o1 = s.add_atom(QueryAtom('O'))
o2 = s.add_atom(QueryAtom('O'))
h = s.add_atom(QueryAtom('H'))
_ = s.add_bond(QueryBond('Double'), c, o1)
_ = s.add_bond(QueryBond('Single'), c, o2)
_ = s.add_bond(QueryBond('Single'), o2, h)

# substructure query for SiO4C
p = QuerySubstructure()
si = p.add_atom(QueryAtom('Si'))
si.num_bonds = 5
o1 = p.add_atom(QueryAtom('O'))
o2 = p.add_atom(QueryAtom('O'))
o3 = p.add_atom(QueryAtom('O'))
o4 = p.add_atom(QueryAtom('O'))
c = p.add_atom(QueryAtom('C'))
c.aromatic = True
_ = p.add_bond(QueryBond('Single'), si, o1)
_ = p.add_bond(QueryBond('Single'), si, o2)
_ = p.add_bond(QueryBond('Single'), si, o3)
_ = p.add_bond(QueryBond('Single'), si, o4)
_ = p.add_bond(QueryBond('Single'), si, c)

# A substructure can also be read in from a ConQuest Connser file.
# filepath = 'monochloropyridine.con'
filepath = 'pentaSi.con'


# To achieve this we make use of the ccdc.search.ConnserSubstructure class.
connser_substructure = ccdc.search.ConnserSubstructure(filepath)


# molecuel Reader
csd_reader = EntryReader('CSD')
ceppiw = csd_reader.molecule('CEPPIW')
aduzor = csd_reader.molecule('ADUZOR')
yamwis = csd_reader.molecule('YAMWIS')
zocxun = csd_reader.molecule('ZOCXUN')
varmik = csd_reader.molecule('VARMIK')

# Setting up and running a substructure search
substructure_search = ccdc.search.SubstructureSearch()
sub_id = substructure_search.add_substructure(connser_substructure)
hits = substructure_search.search(max_hits_per_structure=1)
print(len(hits))  
for hit in hits:
    print(hit.identifier)
mols = hits.superimpose()




entries = ['ceppiw', 'aduzor', 'yamwis', 'zocxun', 'varmik']

# print(ceppiw.smiles)


#analysis_engine = GeometryAnalyser()
#checked_mol = analysis_engine.analyse_molecule(yigpio01)
#for tor in checked_mol.analysed_torsions:
#    if tor.unusual:
#        print('%s: %d %.2f' % (', '.join(tor.atom_labels), tor.nhits, tor.local_density)) 