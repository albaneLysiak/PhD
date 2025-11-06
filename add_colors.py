# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:19:18 2020

@author: admin-user
"""

def is_insertion(levenshtein, length_difference) :
    boo = False
    if  levenshtein == 1 and length_difference == 1 :
        boo = True
    return(boo)

def is_deletion(levenshtein, length_difference) :
    boo = False
    if  levenshtein == 1 and length_difference == -1 :
        boo = True
    return(boo)

def is_substitution(levenshtein, length_difference) :
    boo = False
    if levenshtein == 1 and length_difference == 0 :
        boo = True
    return(boo)

def is_imprecise_realignable_dm(prefixe, suffixe, baitsize, hitsize, hitinbait, baitinhit, liste, line) :
    index = 0
    if suffixe == hitsize :
        index = 1
    elif prefixe == hitsize :
        index = 2
    elif suffixe == baitsize :
        index = 3
    elif prefixe ==  baitsize :
        index = 4
    elif prefixe+suffixe == hitsize and not hitinbait and not baitinhit :
        index = 5
    elif prefixe+suffixe == baitsize and not baitinhit and not hitinbait :
        index = 6
    else :
        index = 7
    return(index)

couple_to_color = {}

tot = 0

couleurs = {}
ct = 0

#with open("links_thr_7_specOMS_no_shift_60_r_haschanged.txt", "r") as psm_file :
with open("links_thr_7_specOMS_shift_60_haschanged.txt", "r") as psm_file :
    liste = []
    psm_file.readline()
    for line in psm_file :
        line_to_write = line
        line = line.replace('"','')
        line = line.replace("\n","")
        rawline = line
        line = line.split("\t")
        bait = line[0]
        hit = line[1]
        couple = str(bait+"/"+hit)
        baitorigin = line[9]
        spc_without_specfit = int(line[11])
        spc_with_specfit = int(line[12])
        dm = round(float(line[6]), 4)
        fpr = float(line[13])
        location = int(line[7])
        levenshtein = float(line[16])
        baitlength = int(line[2])
        hitlength = int(line[3])
        length_difference = int(baitlength)-int(hitlength)
        prefixe = int(line[14])
        suffixe = int(line[15])
        bait_in_hit = line[22]
        hit_in_bait = line[23]
        chaine=bait+"\t"+hit+"\t"+str(dm)+"\t"+str(prefixe)+"\t"+str(suffixe)+"\t"+str(levenshtein)+"\t"+hit_in_bait+"\t"+bait_in_hit
        interesting_chain = bait+"\t"+hit+"\t"+str(dm)
        if baitlength - hitlength > 0 :
            small_size = hitlength
        if baitlength - hitlength < 0 :
            small_size = baitlength
        if baitlength == hitlength :
            small_size = baitlength
        if bait_in_hit == "1" :
            baitinhit = True
        else :
            baitinhit = False
        if hit_in_bait == "1" :
            hitinbait = True
        else :
            hitinbait = False
        index = is_imprecise_realignable_dm(prefixe, suffixe, baitlength, hitlength, hitinbait, baitinhit, liste, chaine)
        if is_insertion(levenshtein, length_difference) : #Insertion ou délétion
            couple_to_color[couple] = "green"
        elif is_deletion(levenshtein, length_difference) :
            couple_to_color[couple] = "green"
        elif is_substitution(levenshtein, length_difference) : #Substitution dun seul résidu
            couple_to_color[couple] = "green"
        elif index in [3,4,6] :
            couple_to_color[couple] = "green"
        elif index in [1,2,5] :
            couple_to_color[couple] = "orange"
        else : #autre cas
            if dm < 0 :
                if spc_with_specfit == baitlength*2 :
                    couple_to_color[couple] = "green"
                else :
                    couple_to_color[couple] = "red"
            if dm > 0 :
                if spc_with_specfit == hitlength*2 :
                    couple_to_color[couple] = "orange"
                else :
                    couple_to_color[couple] = "red"
            if dm == 0 :
                couple_to_color[couple] = "red"
        couleur = couple_to_color[couple]
        if baitorigin != "Decoy" and baitorigin != "Multiple" :
            ct += 1
            try :
                couleurs[couleur] += 1
            except KeyError :
                couleurs[couleur] = 1

print(ct)
print(couleurs)

with open("links_thr_7_specOMS_no_shift_60_r_haschanged.txt","r") as fichier :
        for line in fichier :
            header = line.replace("\n","")
            break

header += "\t"+"color"+"\n"

#fichier2 = open("links_thr_7_specOMS_no_shift_60_r_haschanged_color.txt","w")
fichier2 = open("links_thr_7_specOMS_shift_60_haschanged_color.txt","w")
fichier2.write(header)

#with open("links_thr_7_specOMS_no_shift_60_r_haschanged.txt","r") as fichier :
with open("links_thr_7_specOMS_shift_60_haschanged.txt","r") as fichier :
        fichier.readline()
        for line in fichier :
            line_to_keep = line.replace("\n","")
            line = line_to_keep.split("\t")
            bait = line[0]
            hit = line[1]
            couple = str(bait+"/"+hit)
            fichier2.write(line_to_keep+"\t"+couple_to_color[couple]+"\n")

fichier2.close()