import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import itertools
import matplotlib.pyplot as plt
from scipy.spatial.distance import seuclidean 
import scipy


df = pd.read_csv('dataset.csv', header = 0)
AA_percents = {}
Distances = []
per = []

for row in df.index:
    key = df.ix[row, 'viral_protein_name'] + ' , ' + df.ix[row, 'virus_species']
    value = ProteinAnalysis(df.ix[row, 'viral_protein_AA_seq']).get_amino_acids_percent()
    AA_percents[key] = pd.DataFrame.from_dict(value, orient='index')
for x,y in itertools.combinations(AA_percents.values(), 2):
    Distances.append(scipy.spatial.distance.euclidean(x,y))

numBins = 125
plt.hist(Distances, numBins,color='green',)
plt.title("Amino Acid Comparison")
plt.xlabel("Amino Acid Sequences")
plt.ylabel("Frequencey ")
#plt.show()




    
