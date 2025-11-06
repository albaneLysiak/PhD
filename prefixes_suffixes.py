# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:07:39 2020

@author: admin-user
"""

def get_shared_prefix_size(peptide1,peptide2) :
    nbr = 0
    a = len(peptide1)
    b = len(peptide2)
    c = min(a,b)
    for i in range(c) :
        if peptide1[i] == peptide2[i] :
            nbr += 1
        else :
            break
    return(nbr)
            

def get_shared_suffix_size(peptide1, peptide2) :
    peptide1 = peptide1[::-1]
    peptide2 = peptide2[::-1]
    nbr = 0
    a = len(peptide1)
    b = len(peptide2)
    c = min(a,b)
    for i in range(c) :
        if peptide1[i] == peptide2[i] :
            nbr += 1
        else :
            break
    return(nbr)






