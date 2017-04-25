import numpy as np
##http://pymatgen.org/_static/Basic%20functionality.html
import pymatgen as mg
structure = mg.Structure.from_file("POSCAR")
m=structure.lattice.matrix
area = np.linalg.norm(np.cross(m[0], m[1]))
print area
