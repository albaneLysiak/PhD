# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 08:59:11 2022

@author: admin-user
"""

import matplotlib.pyplot as plt
import statistics

seuils = []
rle_bait_t = []
rle_hit_t = []
rle_bait_d = []
rle_hit_d = []
rle_bait = []
rle_hit = []

for f in ["links_thr_7_specOMS_no_shift_60_r_haschanged_color.txt"] :
#for f in ["links_thr_7_specOMS_shift_60_haschanged_color.txt"] :
        print(f)
        for seuil in range(7,21) :
        #for seuil in range(7,41) :
            rle_bait_t_temp = []
            rle_hit_t_temp = []
            rle_bait_d_temp = []
            rle_hit_d_temp = []
            rle_bait_temp = []
            rle_hit_temp = []
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
                    rle1 = float(line[18])
                    rle2 = float(line[19])
                    #18/19 : RLE ; 20/21 : diversite
                    if baitorigin != "Decoy" and baitorigin != "Multiple" and spc_without_shift >= seuil :
                    #if baitorigin != "Decoy" and baitorigin != "Multiple" and spc_with_shift >= seuil :
                        if hitorigin == "Target" :
                            rle_bait_t_temp.append(rle1)
                            rle_hit_t_temp.append(rle2)
                        elif hitorigin == "Decoy" :
                            rle_bait_d_temp.append(rle1)
                            rle_hit_d_temp.append(rle2)
                        rle_bait_temp.append(rle1)
                        rle_hit_temp.append(rle2)
            rle_bait_t.append(statistics.mean(rle_bait_t_temp))
            rle_hit_t.append(statistics.mean(rle_hit_t_temp))
            rle_bait_d.append(statistics.mean(rle_bait_d_temp))
            rle_hit_d.append(statistics.mean(rle_hit_d_temp))
            rle_bait.append(statistics.mean(rle_bait_temp))
            rle_hit.append(statistics.mean(rle_hit_temp))

# Initialise the figure and axes.
fig, ax = plt.subplots(1, figsize=(8, 6))

'''
print(rle_bait_t)
print(rle_hit_t)
print(rle_bait_d)
print(rle_hit_d)
'''

# Set the title for the figure
#fig.suptitle('Taux de compression RLE selon le seuil de SPC des PSMs target et decoy (PSM1)', fontsize=15)
#fig.suptitle('Diversité en résidus selon le seuil de SPC des PSMs target et decoy (PSM1)', fontsize=15)

# Draw all the lines in the same plot, assigning a label for each one to be
# shown in the legend.
ax.plot(seuils, rle_bait_t, '--', color="blue", label="baits (PSMs target)")
ax.plot(seuils, rle_hit_t, color="lightseagreen", label="hits (PSMs target)")
ax.plot(seuils, rle_bait_d, ':', color="black", label="baits (PSMs decoy)")
ax.plot(seuils, rle_hit_d, color="grey", label="hits (PSMs decoy)")

#ax.plot(seuils, rle_bait, color="blue", label="Baits")
#ax.plot(seuils, rle_hit, color="grey", label="Hits")

#lignes ci-dessous à modifier selon que l'on calcukle la diversité ou bien le taux de compression RLE

# Add a legend, and position it on the lower right (with no box)
plt.legend(loc="upper left", frameon=False, fontsize = 10)
#plt.legend(loc="upper right", frameon=False)
plt.ylabel("Taux de compression RLE (moy)")
#plt.ylabel("Diversité en résidus (moy)")
plt.xlabel("Min raw SPC")
#plt.xlabel("Min shift SPC")

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.show()