# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 17:52:26 2022

@author: admin-user
"""
import networkx as nx
import collections
import matplotlib.pyplot as plt
import statistics
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.axis import Axis

#================ Création du graphe à partir du fichier toutes solutions (PSMa) ================

fichier = "specOMS_shift_all_solutions.csv"

G = nx.Graph()

origins = {}
names = {}

ori = []

with open(fichier, "r") as input_file :
    input_file.readline()
    i = 0
    for line in input_file :
        i += 1
        line = line.split(";")
        pep1 = line[0]
        pep2 = line[1]
        or1 = line[10].replace("\n", "")
        or1 = or1.replace("Contaminant and Target","Target")
        or1 = or1.replace("Contaminant","Target")
        or2 = line[9]#.replace("\n", "")
        or2 = or2.replace("Contaminant and Target","Target")
        or2 = or2.replace("Contaminant","Target")
        or2 = or2.replace("Multiple","Decoy")
        spc = float(line[2])
        #rle1 = float(line[14])
        #rle2 = float(line[15])
        #if not(rle1 >= 1.5 or rle2 >= 1.5) and spc >= 8 :
        if or1 != "Decoy" and or1 != "Multiple" : #and spc >= 10 :
            G.add_edge(pep1,pep2)
            origins[pep1] = or1
            origins[pep2] = or2
            ori.append(or1)
            ori.append(or2)

print(G.number_of_nodes())
print(G.number_of_edges())

nx.set_node_attributes(G, origins, "origin")

'''
Deux principales possibilités de graphe : 1)le graphe complet 2)le graphe filtré selon le spc et le degré
Filtrer selon spc : ligne "if or1 != "Decoy" and or1 != "Multiple" : #and spc >= 10 :" boucle précédente
Filtrer selon degré : décommenter les deux boucles for suivantes
spc 10 et degré 5 : graphe du manuscrit
'''

'''
for node in list(G.nodes) :
    if G.degree[node] < 5 :
        G.remove_node(node)

for node in list(G.nodes) :
    if G.degree[node] == 0 :
        G.remove_node(node)
'''

print(G.number_of_nodes())

#Ecriture du graphe dans un fichier lisible par Gephi
nx.write_gexf(G, "graphe.gexf")

'''
Recréer le graphe avec Gephi
1) Ouvrir "graphe.gexf" sous Gephi
2) Noeuds -> partitions -> origin, mettre target en bleu et decoy en rouge, appliquer
3) Spatialisation : früchterman reingold, exécuter
'''

degrees = {}

for node in G.nodes() :
    try :
        degrees[G.degree(node)] += 1
    except KeyError :
        degrees[G.degree(node)] = 1

degrees = collections.OrderedDict(sorted(degrees.items()))

print(degrees)

#================ Affichage de l'histogramme des degrés ================

#voir conseils https://towardsdatascience.com/histograms-with-pythons-matplotlib-b8b768da9305

degrees = []

degrees_t = []
degrees_d = []

for node in G.nodes() :
    degrees.append(G.degree(node))
    if origins[str(node)] ==  "Target" :
        degrees_t.append(G.degree(node))
    elif origins[str(node)] ==  "Decoy" :
        degrees_d.append(G.degree(node))

print(statistics.mean(degrees))
print(statistics.mean(degrees_t))
print(statistics.mean(degrees_d))

fig = plt.figure(figsize=(16,6))

#n, bins, patches = plt.hist(degrees, bins = 25)
b2 = [i for i in range(1,146,5)]
b = [i for i in range(1,146)]
b[0] = 1
b2[0] = 1
n, bins, patches = plt.hist(degrees, bins = b)
plt.xticks(b)

ax = plt.gca()
locator = MultipleLocator(5)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(MultipleLocator(1))

plt.xlim(left = 0, right = 144)

#plt.xscale('log')
plt.yscale('log')

#plt.legend(loc="center right", frameon=False)
plt.ylabel("Distribution du degré des noeuds du graphe de peptides")
plt.ylabel("Nombre de n"+"\u0153"+"uds")
plt.xlabel("Degré")

#grid
facecolor = '#EAEAEA' #blanc cassé
color_bars = '#3475D0' #bleu
plt.grid(axis='y', color=color_bars, lw = 0.5, alpha=0.7)
plt.grid(color='white', lw = 0.5, axis='x', which = 'both')

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

plt.show()

#print(max(degrees))