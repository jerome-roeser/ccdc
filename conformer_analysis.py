from ccdc.io import EntryReader
from ccdc.conformer import GeometryAnalyser


csd_reader = EntryReader('CSD')
yigpio01 = csd_reader.molecule('YIGPIO01')

analysis_engine = GeometryAnalyser()
checked_mol = analysis_engine.analyse_molecule(yigpio01)
for tor in checked_mol.analysed_torsions:
    if tor.unusual:
        print('%s: %d %.2f' % (', '.join(tor.atom_labels), tor.nhits, tor.local_density)) 