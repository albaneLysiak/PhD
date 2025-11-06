# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:38:40 2020

@author: admin-user
"""

def get_aa_diversity(peptide) :
    aas = []
    for aa in peptide :
        if aa not in aas :
            aas.append(aa)
    #nbre d'aa non redondants sur nomre d'aa total dans le peptide
    return(len(aas)/len(peptide))