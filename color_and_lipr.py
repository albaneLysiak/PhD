# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:35:20 2020

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
    #Détermine certains cas Verts et Oranges
    index = 0
    if suffixe == hitsize :#Orange car le hit est le suffixe du bait
        index = 1
    elif prefixe == hitsize :#Orange car le hit est le préfixe du bait
        index = 2
    elif suffixe == baitsize : #Vert car le bait est le suffixe du hit
        index = 3
    elif prefixe ==  baitsize : #Vert car le bait est le préfixe du hit
        index = 4
    elif prefixe+suffixe == hitsize and not hitinbait and not baitinhit :
        #Orange car les deux morceaux du hit correspondent au préfixe et suffixe du bait
        index = 5
    elif prefixe+suffixe == baitsize and not baitinhit and not hitinbait :
        # Vert car les deux morceaux du bait correspondent au préfixe et suffixe du hit
        index = 6
    else :
        index = 7
    return(index)

#written_file = open("colors_lipr_ss1.csv","w")
#written_file = open("colors_lipr_ss2.csv","w")
#written_file = open("colors_lipr_psm1.csv","w")
written_file = open("colors_lipr_psm2.csv","w")
written_file.write("Min shift spc"+";"+"Greens"+";"+"Oranges"+";"+"Reds"+";"+"Total"+";"+"LIPR(avg)"+"\n")

for seuil in range(7,8) :
    #si on veut calculer pour tous les seuils, mettre range(7, 21)
    print(seuil)
    greenI_PSM_to_dm = {}
    greenD_PSM_to_dm = {}
    greenS_PSM_to_dm = {}
    green346_PSM_to_dm = {}
    green_others_PSM_to_dm = {}
    orange135_to_dm = {}
    orange_others_to_dm = {}
    red_PSM_dm_not_nul_to_dm = {}
    red_PSM_dm_nul_to_dm = {}
    lipr_sum = 0
    #with open("links_thr_7_specOMS_no_shift_60_r_haschanged.txt", "r") as psm_file : #fichier à prendre en entrée
    with open("links_thr_7_specOMS_shift_60_haschanged.txt", "r") as psm_file : #fichier à prendre en entrée
        #no shift pour strat_raw, shift pour strat_shift
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
            has_changed = line[26]
            spc_without_specfit = int(line[11])
            spc_with_specfit = int(line[12])
            try :
                lipr = float(line[13])
            except ValueError :
                pass
            if baitorigin != "Decoy" and baitorigin != "Multiple" and spc_with_specfit >= seuil : #and has_changed == '1' :
                #commenter "has_changed" si on veut psm1 ou psm2 et non ss1 ou ss2
                lipr_sum += lipr
                classification = ""
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
                if is_insertion(levenshtein, length_difference) :
                    greenI_PSM_to_dm[interesting_chain] = dm
                    classification = "insertion"
                elif is_deletion(levenshtein, length_difference) :
                    greenD_PSM_to_dm[interesting_chain] = dm
                    classification = "deletion"
                elif is_substitution(levenshtein, length_difference) :
                    classification = "substitution"
                    greenS_PSM_to_dm[interesting_chain] = dm
                elif index in [3,4,6] :
                    classification = "case346"
                    green346_PSM_to_dm[interesting_chain] = dm
                elif index in [1,2,5] :
                    classification = "orange125"
                    orange135_to_dm[interesting_chain] = dm
                else : #autre cas
                    if dm < 0 :
                        if spc_with_specfit == baitlength*2 :
                            green_others_PSM_to_dm[interesting_chain] = dm
                            classification = "big_neg_dm"
                        else :
                            red_PSM_dm_not_nul_to_dm[interesting_chain] = dm
                            classification = "red"
                    if dm > 0 :
                        if spc_with_specfit == hitlength*2 :
                            classification = "orange_others"
                            orange_others_to_dm[interesting_chain] = dm
                        else :
                            classification = "red"
                            red_PSM_dm_not_nul_to_dm[interesting_chain] = dm
                    if dm == 0 :
                        red_PSM_dm_nul_to_dm[interesting_chain] = dm
                        classification = "rednul"
    #on calcule les couleurs des PSMs
    #Verts : insertions, délétions, substitution
    greens = len(greenI_PSM_to_dm.keys()) + len(greenD_PSM_to_dm.keys()) + len(greenS_PSM_to_dm.keys()) + len(green346_PSM_to_dm.keys()) + len(green_others_PSM_to_dm.keys())
    oranges = len(orange_others_to_dm.keys()) + len(orange135_to_dm.keys())
    reds = len(red_PSM_dm_not_nul_to_dm.keys()) + len(red_PSM_dm_nul_to_dm.keys())
    tot = greens + oranges + reds
    g_tot_per = round((greens/tot)*100,2)
    o_tot_per = round((oranges/tot)*100,2)
    red_tot_per = round((reds/tot)*100,2)
    lipr_avg = round((lipr_sum/tot),2)
    
    written_file.write(str(seuil)+";"+str(greens)+";"+str(oranges)+";"+str(reds)+";"+str(tot)+";"+str(lipr_avg)+"\n")
    #written_file.write(str(seuil)+";"+str(greens)+"/"+str(g_tot_per)+";"+str(oranges)+"/"+str(o_tot_per)+";"+str(reds)+"/"+str(red_tot_per)+";"+str(tot)+";"+str(lipr_avg)+"\n")

written_file.close()
