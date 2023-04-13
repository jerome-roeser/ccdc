import ccdc.search
#import ccdc.io
import os

from ccdc.io import EntryReader
from ccdc.io import MoleculeReader
from ccdc.conformer import GeometryAnalyser

from ccdc.search import QueryAtom
from ccdc.search import QueryBond
from ccdc.search import QuerySubstructure

from ccdc import io
from ccdc import conformer
from ccdc.conformer import GeometryAnalyser


csd_reader = EntryReader('CSD')
ceppiw = csd_reader.molecule('CEPPIW')
mol = ceppiw

engine = conformer.GeometryAnalyser()
print(engine.settings.summary())



# disable non-neede analyses
engine.settings.angle.analyse = False
engine.settings.bond.analyse = False
engine.settings.ring.analyse = False


geometry_analysed_mol = engine.analyse_molecule(mol)

[t.atom_labels for t in engine.analyse_molecule(mol).analysed_torsions]