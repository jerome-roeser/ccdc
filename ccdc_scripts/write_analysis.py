# Let us write out the molecules from these hits as a multi-mol2 file.
# As a preamble let us set up a variable for a temporary directory.
from ccdc.utilities import _test_output_dir
tempdir = _test_output_dir()

output_file = os.path.join(tempdir, 'pentaSi_hits.mol2')
with ccdc.io.MoleculeWriter(output_file) as writer:
    for m in mols:
        writer.write(m)
#We can also write the result data into a ConQuest to Mercury interchange file, so that the results, with constraints and measurements may be analysed in the data analysis module of Mercury.

hits.write_c2m_file(os.path.join(tempdir, 'pentaSi_hits.c2m'))
#We can find the matched atoms for each hit, where the hit atoms have coordinates: