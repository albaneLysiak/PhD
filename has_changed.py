# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:45:29 2020

@author: admin-user
"""

bait_to_hit_no_shift = {}
bait_to_hit_shift = {}

#lecture des deux fichiers
with open("links_thr_7_specOMS_no_shift_60.txt","r") as fichier :
    fichier.readline()
    for line in fichier :
        line = line.split("\t")
        bait = line[0]
        hit = line[1]
        bait_to_hit_no_shift[bait] = hit

with open("links_thr_7_specOMS_shift_60.txt","r") as fichier :
    fichier.readline()
    for line in fichier :
        line = line.split("\t")
        bait = line[0]
        hit = line[1]
        bait_to_hit_shift[bait] = hit

bait_to_is_different = {}

#comptage du nombre de baits pour lesquels le hit est différent entre les deux stratégies
for elt in bait_to_hit_no_shift.keys() :
    if bait_to_hit_no_shift[elt] != bait_to_hit_shift[elt] :
        bait_to_is_different[elt] = 1
    else :
        bait_to_is_different[elt] = 0

with open("links_thr_7_specOMS_no_shift_60.txt","r") as fichier :
        for line in fichier :
            header = line.replace("\n","")
            break

header += "\t"+"has_changed"+"\n"

#écriture du nombre dans les fichiers résultats
fichier2 = open("links_thr_7_specOMS_no_shift_60_r_haschanged.txt","w")
fichier2.write(header)

with open("links_thr_7_specOMS_no_shift_60_r.txt","r") as fichier :
        fichier.readline()
        for line in fichier :
            line_to_keep = line.replace("\n","")
            line = line_to_keep.split("\t")
            bait = line[0]
            fichier2.write(line_to_keep+"\t"+str(bait_to_is_different[bait])+"\n")

fichier2.close()

fichier2 = open("links_thr_7_specOMS_shift_60_haschanged.txt","w")
fichier2.write(header)

with open("links_thr_7_specOMS_shift_60.txt","r") as fichier :
        fichier.readline()
        for line in fichier :
            line_to_keep = line.replace("\n","")
            line = line_to_keep.split("\t")
            bait = line[0]
            fichier2.write(line_to_keep+"\t"+str(bait_to_is_different[bait])+"\n")
                
fichier2.close()