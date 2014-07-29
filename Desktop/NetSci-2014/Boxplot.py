import pandas as pd
import matplotlib.pyplot as plt
ongc_list = []
beng_list = []
df = pd.read_csv('dataset.csv', header = 0)
for row in df.index:
    if df.ix[row, 'virus_species_oncogenic'] == 0:
       beng_list.append(len(df.ix[row, 'viral_protein_AA_seq']))
    elif df.ix[row, 'virus_species_oncogenic'] == 1:
         ongc_list.append(len(df.ix[row, 'viral_protein_AA_seq']))
data = [ongc_list,beng_list]
plt.boxplot(data)
labels = ('Oncogenic', 'Non-Oncogenic')
plt.legend()
plt.xticks(range(1,3),labels, rotation=15)
plt.xlabel('Ocogenicity')
plt.ylabel('Length of the Amino Acid Sequence')
plt.title('The Lengtj of the amino acid sequence in oncogenic and non-oncogenic viral proteins')
plt.show()
