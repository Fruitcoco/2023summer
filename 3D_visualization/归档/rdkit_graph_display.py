from rdkit import Chem
from plotly.offline import init_notebook_mode, iplot, offline
from xyz2graph import MolGraph, to_plotly_figure

molAfile = '20667_sybyl.mol2'
fxyz = 'molA.xyz'
mol = Chem.MolFromMol2File(molAfile, removeHs=False)
Chem.MolToXYZFile(mol, fxyz)
# Initiate the Plotly notebook mode
init_notebook_mode(connected=True)
# Create the MolGraph object
mg = MolGraph()
# Read the data from the .xyz file
mg.read_xyz(fxyz)
# Create the Plotly figure object
fig = to_plotly_figure(mg)
# Plot the figure
offline.plot(fig)
# Plot the figure
iplot(fig)