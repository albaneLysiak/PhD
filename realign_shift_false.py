# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:48:49 2020

@author: admin-user
"""

couple_to_spc = {}
    
with open("specOMS_shift_all_solutions.csv", "r") as all_solutions :
    all_solutions.readline()
    for line in all_solutions :
        line = line.split(";")
        bait = line[0]
        hit = line[1]
        spc_with_specfit = line[3]
        couple = bait+"/"+hit
        couple_to_spc[couple] = spc_with_specfit
        
with open("links_thr_7_specOMS_no_shift_60.txt", "r") as psm_file :
    for line in psm_file :
        header = line
        break

corrected_file = open("links_thr_7_specOMS_no_shift_60_r.txt","w")

corrected_file.write(header)

with open("links_thr_7_specOMS_no_shift_60.txt", "r") as psm_file :
    psm_file.readline()
    for line in psm_file :
        line = line.split("\t")
        first_part = line[0:12]
        second_part = line[13:len(line)+1]
        first_str = ""
        for elt in first_part :
            first_str += "\t" + elt
        first_str = first_str.lstrip("\t")
        scd_str = ""
        for elt in second_part :
            scd_str += "\t" + elt
        bait = line[0]
        hit = line[1]
        couple = str(bait+"/"+hit)
        spc_with_specfit = couple_to_spc[couple]
        reconstituted_line = first_str + "\t" + spc_with_specfit + scd_str
        corrected_file.write(reconstituted_line)
        
corrected_file.close()
