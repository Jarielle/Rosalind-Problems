import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.spatial.distance import seuclidean 
import scipy
import networkx as nx
from pylab import *

#df = pd.read_csv('../data/dataset.csv', header = 0)
df = pd.read_csv('dataset.csv', header = 0)
AA_percents = {}
Distances = []
for row in df.index:
    key = df.ix[row, 'viral_protein_name'] + ' : ' + df.ix[row, 'virus_species']
    value = ProteinAnalysis(df.ix[row, 'viral_protein_AA_seq']).get_amino_acids_percent()
    AA_percents[key] = pd.DataFrame.from_dict(value, orient='index')
Distances = {}
for x,y in itertools.combinations(AA_percents.keys(), 2):
    Distances[x,y] = scipy.spatial.distance.euclidean(AA_percents[x], AA_percents[y])

my_list = []
pos_edges = []
e069 = []

for x,y in Distances.items():
    for z in x:
        my_list.append(z)
    PE = x + (y,)
    pos_edges.append(PE)
proteins = list(set(my_list))
for edge in pos_edges:
    for weight in edge:
        if .000<= weight <.069:
           e069.append(edge)
        else:
            pass
G = nx.DiGraph()
G.add_nodes_from(proteins)
pos=nx.spring_layout(G)
G.add_weighted_edges_from(e069, weight='weight')
G_ud = G.to_undirected()
numBins = 15
plt.hist(G.degree().values(), numBins,color='#00CCCC')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")
plt.savefig('Degree Distribution.png')
#plt.show()
