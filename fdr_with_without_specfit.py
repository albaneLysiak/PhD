# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:12:40 2020

@author: admin-user
"""

#diversity_thr = 0.55

'''
Calcule le FDR pour les 3 catégories de deltaM, et pour tous les PSMs
'''

with open("fdr_thr_dm_psm2.csv","w") as file :
    #file.write("Min spc"+";"+"FDR"+";"+"VP"+";"+"FP"+"\n")
    file.write(";dm=0;;dm<0;;dm>0;;Total\n")
    file.write("Min spc;Target;Decoy;Target;Decoy;Target;Decoy;Target;Decoy;FDR\n")
    for f in ["links_thr_7_specOMS_shift_60_haschanged_color.txt"] :
            '''
            Pour strat_raw, "links_thr_7_specOMS_no_shift_60_r_haschanged_color.txt"
            Pour strat_shift, "links_thr_7_specOMS_shift_60_haschanged_color.txt"
            '''
            print(f)
            #for seuil in range(7,21) :
            for seuil in range(7,41,2) :
                '''
                Pour strat_raw, de 7 à 21
                Pour strat_shift, de 7 à 41
                '''
                false_links_list=[]
                false_links_list_pos=[]
                false_links_list_neg=[]
                false_links_list_null=[]
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
                        hit_diversity = float(line[21])
                        if baitorigin != "Decoy" and baitorigin != "Multiple" and spc_with_shift >= seuil :
                            '''
                            Pour strat_raw, mettre "spc_without_shift >= seuil"
                            Pour strat_shift, mettre "spc_with_shift >= seuil"
                            '''
                            deltam=float(line[6])
                            if hitorigin == "Decoy" :
                                false_links_list.append(False)
                            else :
                                false_links_list.append(True)
                            if deltam>0 :
                                if hitorigin == "Decoy" :
                                    false_links_list_pos.append(False)
                                else :
                                    false_links_list_pos.append(True)
                            elif deltam<0 :
                                if hitorigin == "Decoy" :
                                    false_links_list_neg.append(False)
                                else :
                                    false_links_list_neg.append(True)
                            elif deltam == 0 :
                                if hitorigin == "Decoy" :
                                    false_links_list_null.append(False)
                                else :
                                    false_links_list_null.append(True)
                fptot = false_links_list.count(False)
                vptot = false_links_list.count(True)
                fppos = false_links_list_pos.count(False)
                vppos = false_links_list_pos.count(True)
                fpneg = false_links_list_neg.count(False)
                vpneg = false_links_list_neg.count(True)
                fpnull = false_links_list_null.count(False)
                vpnull = false_links_list_null.count(True)
                
                fdrtot = (fptot/len(false_links_list))*100
                fdrpos = (fppos/len(false_links_list_pos))*100
                fdrneg = (fpneg/len(false_links_list_neg))*100
                fdrnull = (fpnull/len(false_links_list_null))*100
                
                print("Seuil de spc = "+str(seuil))
                print("FDR total = "+str(fdrtot))
                #file.write(str(seuil)+";"+str(round(fdrtot,2))+";"+str(vptot)+";"+str(fptot)+"\n")
                file.write(str(seuil)+";"+str(vpnull)+";"+str(fpnull)+";"+str(vpneg)+";"+str(fpneg)+";"+str(vppos)+";"+str(fppos)+";"+str(vptot)+";"+str(fptot)+";"+str(round(fdrtot,2))+"\n")
                #print("FDR pos = "+str(fdrpos))
                #print("FDR neg = "+str(fdrneg))
                #print("FDR nul = "+str(fdrnull))
                
            