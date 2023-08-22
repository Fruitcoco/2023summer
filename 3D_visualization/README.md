# molgraph
[**mol2graph**] is a Python package for reading .mol2 files and constructing of molecular graphs from mol output files. This package is built upon xyz2graph package by Mykola Zotko. It adds the features of Atom type, Atom name and bond type to the 3D visualization and it tries to put 2 molecula into one graph to compare the similarity of molecula.

The molecular graph can be converted into [NetworkX](https://networkx.github.io) graph or [Plotly](https://plot.ly) figure for 3D visualization in a browser window or in a [Jupyter notebook](https://jupyter.org).

Looking forward
I find it is hard to implement the interaction bewteen two input molecula. The next step is to be able to read mapping information and the mapped atom can be visualized. Also, it would be helpful to hide one molecula from the other but this may requires change in plotly package which may need help from front end developer.  


<p align="center">
  <img src="images/mol.gif",  width="1024">
</p>picture

## Requirements
 * **Python 3**
 * [NumPy](https://numpy.org)
 * [NetworkX](https://networkx.github.io)
 * [Plotly](https://plot.ly)
 

## Usage
```
from mol2graph.molgraph import MolGraph 
from mol2graph.vis_helper import to_plotly_figure,to_networkx_graph
from plotly.offline import init_notebook_mode, iplot

# Create the MolGraph object
mg = MolGraph()

# Read the data from the .mol2 file
mg.read_xyz(file_path)

# Create the Plotly figure object
fig = to_plotly_figure(mg)[0]

# Plot the figure
offline.plot(fig)

# Convert the molecular graph to the NetworkX graph
G = to_networkx_graph(mg)
```

## Usage in Jupyter Notebook

```
from mol2graph.molgraph import MolGraph 
from mol2graph.vis_helper import to_plotly_figure,to_networkx_graph
from plotly.offline import init_notebook_mode, iplot

# Initiate the Plotly notebook mode
init_notebook_mode(connected=True)

# Create the MolGraph object
mg = MolGraph()

# Read the data from the .mol2 file
mg.read_xyz(file_path)

# Create the Plotly figure object
fig = to_plotly_figure(mg)[0]

# Plot the figure
iplot(fig)
```

