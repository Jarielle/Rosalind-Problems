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
x = nx.betweenness_centrality(G).values()
y = nx.closeness_centrality(G).values()
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1,1,1) 
ax.set_title("Amini Acid Comparison")
ax.set_xlabel("Betweenness Centrality")
ax.set_ylabel("Closeness Centrality")
ax.set_xlim([-.0001,.005])
ax.set_ylim([.00,.3])
fit = polyfit(x,y,1)
fit_fn = poly1d(fit)
ax.plot(x,y, 'yo', x, fit_fn(x), '--k')
fig.savefig('Scatter Plot.png')
