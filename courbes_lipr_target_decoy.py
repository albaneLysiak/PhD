# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 08:59:11 2022

@author: admin-user
"""

import matplotlib.pyplot as plt
import statistics

seuils = []
lipr_t = []
lipr_d = []

'''
with open("psm1_lipr_target_decoy.txt") as fichier :
    fichier.readline()
    for line in fichier :
        #print(line)
        line = line.split("\t")
        seuils.append(float(line[0]))
        lipr_t.append(float(line[2]))
        lipr_d.append(float(line[3]))
        
print(seuils)
print(lipr_t)
print(lipr_d)
'''

for f in ["links_thr_7_specOMS_no_shift_60_r_haschanged_color.txt"] :
        print(f)
        for seuil in range(7,21) :
            target = []
            decoy = []
            seuils.append(seuil)
            with open(f,"r") as fichier :
                fichier.readline()
                for line in fichier :
                    line = line.replace('"','')
                    line = line.replace("\n","")
                    line=line.split("\t")
                    baitorigin = line[9]
                    hitorigin = line[10]
                    spc_without_shift = float(line[11])
                    spc_with_shift = float(line[12])
                    try :
                        lipr = float(line[13])
                    except ValueError :
                        pass
                    if baitorigin != "Decoy" and baitorigin != "Multiple" and spc_without_shift >= seuil : #and hit_diversity < diversity_thr :
                        if hitorigin == "Target" :
                            target.append(lipr)
                        elif hitorigin == "Decoy" :
                            decoy.append(lipr)
                lipr_t.append(statistics.mean(target))
                lipr_d.append(statistics.mean(decoy))

# Initialise the figure and axes.
fig, ax = plt.subplots(1, figsize=(8, 6))

# Set the title for the figure
#fig.suptitle('LIPR selon le seuil de SPC des PSMs target et decoy (PSM1)', fontsize=15)

# Draw all the lines in the same plot, assigning a label for each one to be
# shown in the legend.
ax.plot(seuils, lipr_t, color="blue", label="PSMs Target")
ax.plot(seuils, lipr_d, color="gray", label="PSMs Decoy")

# Add a legend, and position it on the lower right (with no box)
#plt.legend(loc="center right", title="Legend Title", frameon=False)
plt.legend(loc="center right", frameon=False)
plt.ylabel("LIPR (moy %)")
plt.xlabel("Min raw SPC")

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.show()