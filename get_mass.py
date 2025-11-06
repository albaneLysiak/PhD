# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:50:43 2020

@author: admin-user
"""

import itertools

#================ Listes des résidus ================

#liste avec résidus + H+ + NT + CT + cystéine carbamidométhylée ($) + asparagine déamidée (@) + acides aspartique avec adduit de sodium (&)
aa_list = ["G","A","S","P","V","T","C","I","N","D","Q","K","E","M","H","F","R","Y","W","U","O","NT","H+","CT","$","@","&"]
#même chose sans NT, CT et H+
aaList2 = ["G","A","S","P","V","T","C","I","N","D","Q","K","E","M","H","F","R","Y","W","U","O","$","@","&"]
#même chose sans résidus modifiés "$","@","&"
aaList3 = ["G","A","S","P","V","T","C","I","N","D","Q","K","E","M","H","F","R","Y","W","U","O"]
#résidus classiques, NT, H+ et CT
aaList4 = ["G","A","S","P","V","T","C","I","N","D","Q","K","E","M","H","F","R","Y","W","U","O","NT","H+","CT"]

#================ Différentes variations des listes de masses ================

#aa classiques + NT, CT, H+ + 3 résidus spéciaux
#'$' = C carbamydométhylée, '@' = N déaminé, '&' = D formylé
#C : cystéine non carbamidométhylée
mass_list = [57.021463721083, 71.037113785565, 87.032028405125, 97.052763850047, 99.068413914529, 101.047678469607, 103.009184785565, 113.084063979011,
114.042927442166,
115.026943024685,
128.058577506648,
128.094963016052,
129.042593089167,
131.040484914529,
137.058911859647,
147.068413914529,
156.101111025652,
163.063328534089,
186.07931295157,
168.964198469607,
255.158291550141,
1.007825032241,
1.007276466879,
15.99491461956 + 1.007825032241,
103.009184785565 + 57.021463721083,
114.042927442166 + 0.9848,
115.026943024685 + 21.981943]

#sans CT, NT et H+, C : cystéine carbamydométhylée
mass_list2 = [57.021463721083, 71.037113785565, 87.032028405125, 97.052763850047, 99.068413914529, 101.047678469607, 103.009184785565+57.021463721083, 113.084063979011,
114.042927442166,
115.026943024685,
128.058577506648,
128.094963016052,
129.042593089167,
131.040484914529,
137.058911859647,
147.068413914529,
156.101111025652,
163.063328534089,
186.07931295157,
168.964198469607,
255.158291550141]

#avec CT, NT et H+, C : cystéine carbamydométhylée
massList = [57.021463721083, 71.037113785565, 87.032028405125, 97.052763850047, 99.068413914529, 101.047678469607, 103.009184785565+57.021463721083, 113.084063979011,
114.042927442166,
115.026943024685,
128.058577506648,
128.094963016052,
129.042593089167,
131.040484914529,
137.058911859647,
147.068413914529,
156.101111025652,
163.063328534089,
186.07931295157,
168.964198469607,
255.158291550141,
1.007825032241,
1.007276466879,
15.99491461956 + 1.007825032241]

#================ Création du dictionnaire résidu vers masse ================

mass_dict = {}

indice = 0
for aa in aaList4 :
    mass_dict[aa] = massList[indice]
    indice += 1

def get_mass(peptide) : #masse d'un peptide total
    mass = 0
    for char in peptide :
        if char != "X" and char != "*" :
            mass += mass_dict[char]
    #mass = mass + mass_dict["NT"] + mass_dict["CT"] + 2*mass_dict["H+"]
    mass = mass + mass_dict["NT"] + mass_dict["CT"]
    return mass

def get_mass_residue(residue) : #masse d'un peptide sans Nter et Cter
    mass = 0
    for char in residue :
        if char != "X" and char != "*" :
            mass += mass_dict[char]
    return mass

def get_mass_aa(aa) : #masse d'un résidu donné
    return mass_dict[aa]

def get_b_mass(seq) : #masse d'un ion b d'une séquence en résidus
    return(round(get_mass_residue(seq)+mass_dict["NT"],2))

def get_y_mass(seq) : #masse d'un ion y d'une séquence en résidus
    return(round(get_mass_residue(seq)+mass_dict["CT"]+mass_dict["NT"]+mass_dict["H+"],2))

#versions non arrondies
def get_b_mass_no_round(seq) :
    #return(get_mass_residue(seq)+mass_dict["NT"])
    return(get_mass_residue(seq)) #+mass_dict["H+"])

def get_y_mass_no_round(seq) :
    return(get_mass_residue(seq)+mass_dict["CT"]+mass_dict["NT"]+mass_dict["H+"])

def get_b_ions(peptide) : #pour un peptide donné, renvoie un dictionnaire masse vers séquence des ions b
    b_dico = {}
    for i in range(1,len(peptide)+1) :
        ion = peptide[0:i]
        b_dico[get_b_mass(ion)] = ion
    return(b_dico)

def get_y_ions(peptide) :#pour un peptide donné, renvoie un dictionnaire masse vers séquence des ions y
    peptide = peptide[::-1]
    y_dico={}
    for i in range(1, len(peptide)+1) :
        ion = peptide[0:i]
        y_dico[get_y_mass(ion)] = ion
    return(y_dico)

#================ Fonctions non utilisées ================

def get_modified_b_ions(peptide, delta, location) :
    b_dico = {}
    if location == 0 :
        for i in range(1,len(peptide)+1) :
            ion = peptide[0:i]
            b_dico[round(get_b_mass_no_round(ion)+delta,4)] = get_modified_model(ion,location)
    else :
        for i in range(1,len(peptide)+1) :
            ion = peptide[0:i]
            if i-1 >= location or location==1 :
                b_dico[round(get_b_mass_no_round(ion)+delta,4)] = get_modified_model(ion,location)
            else :
                b_dico[get_b_mass(ion)] = ion
    return(b_dico)

def get_modified_y_ions(peptide, delta, location) :
    peptide = peptide[::-1]
    rv_location = len(peptide)-location+1
    y_dico={}
    if rv_location == 0 :
        for i in range(1,len(peptide)+1) :
            ion = peptide[0:i]
            y_dico[round(get_y_mass_no_round(ion)+delta,4)] = get_modified_model(ion,rv_location)
    else :
        for i in range(1,len(peptide)+1) :
            ion = peptide[0:i]
            if i-1 >= rv_location or rv_location==1 :
                y_dico[round(get_y_mass_no_round(ion)+delta,4)] = get_modified_model(ion,rv_location)
            else :
                y_dico[get_y_mass(ion)] = ion
    return(y_dico)

def get_modified_model(ion, location) :
    new_ion = ""
    if location != len(ion) :
        for i in range(len(ion)) :
            if i == location :
                new_ion += "*"+ion[i]
            else :
                new_ion += ion[i]
    else :
        new_ion = ion+"*"
    return(new_ion)

def get_delta_fpr(bait, hit, dm, location, precision) :
    bait_b_ions = get_b_ions(bait)
    bait_y_ions = get_y_ions(bait)
    hit_b_ions = get_modified_b_ions(hit, dm, location)
    hit_y_ions = get_modified_y_ions(hit, dm, location)
    '''
    print(bait_b_ions)
    print("============================================")
    print(bait_y_ions)
    print("============================================")
    print(hit_b_ions)
    print("============================================")
    print(hit_y_ions)
    '''
    spc=[]
    wrong_peaks=0
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1 < elt2+precision and elt1 > elt2-precision :
                #print(elt1,elt2)
                print(elt1,bait_b_ions[elt1],"<--->",elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_b_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_b_ions[elt1])
                    #print(elt2,hit_b_ions[elt2])
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1 < elt2+precision and elt1 > elt2-precision :
                #print(elt1,elt2)
                print(elt1,bait_b_ions[elt1],"<--->",elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_y_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_b_ions[elt1])
                    #print(elt2,hit_y_ions[elt2])
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1 < elt2+precision and elt1 > elt2-precision :
                #print(elt1,elt2)
                print(elt1,bait_y_ions[elt1],"<--->",elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_b_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_y_ions[elt1])
                    #print(elt2,hit_b_ions[elt2])
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1 < elt2+precision and elt1 > elt2-precision :
                #print(elt1,elt2)
                print(elt1,bait_y_ions[elt1],"<--->", elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_y_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_y_ions[elt1])
                    #print(elt2,hit_y_ions[elt2])
    spc = set(spc)
    #return(len(spc))
    #print(wrong_peaks)
    #print(spc)
    #false_peaks_rate = (wrong_peaks/len(spc))*100
    return(len(spc))

#================ Fin fonctions non utilisées ================

#================ Fonctions liées au LIPR ================

def get_false_peaks_rate0(bait, hit) : #détermine le LIPR entre un bait et un hit
    bait_b_ions = get_b_ions(bait)
    bait_y_ions = get_y_ions(bait)
    hit_b_ions = get_b_ions(hit)
    hit_y_ions = get_y_ions(hit)
    spc=[]
    wrong_peaks=0
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_b_ions[elt1])
                #print(elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_b_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_b_ions[elt1])
                    #print(elt2,hit_b_ions[elt2])
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_b_ions[elt1])
                #print(elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_y_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_b_ions[elt1])
                    #print(elt2,hit_y_ions[elt2])
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_y_ions[elt1])
                #print(elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_b_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_y_ions[elt1])
                    #print(elt2,hit_b_ions[elt2])
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_y_ions[elt1])
                #print(elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_y_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_y_ions[elt1])
                    #print(elt2,hit_y_ions[elt2])
    #spc = set(spc)
    #return(len(spc))
    #print(wrong_peaks)
    #print(spc)
    false_peaks_rate = (wrong_peaks/len(spc))*100
    return(false_peaks_rate)
    """
    print(spc)
    try :
        false_peaks_rate = (wrong_peaks/spc)*100
        return(false_peaks_rate)
    except ZeroDivisionError :
        return("X")
    """

def get_false_peaks_rate(bait, hit) : #détermine le LIPR entre un bait et un hit
    '''
    différence avec fonction précédente : si deux séquences différentes ont la même masse m1
    on ne les compte pas dans le LIPR si deux séquences identiques ont cette même masse m1
    sinon le LIPR est surestimé
    '''
    bait_b_ions = get_b_ions(bait)
    bait_y_ions = get_y_ions(bait)
    hit_b_ions = get_b_ions(hit)
    hit_y_ions = get_y_ions(hit)
    spc=[]
    vp_masses = []
    fp_masses = []
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_b_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_y_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_b_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_y_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    false_peaks = 0
    spc = set(spc)
    for elt in set(fp_masses) :
        if elt not in vp_masses :
            false_peaks += 1
    false_peaks_rate = (false_peaks/len(spc))*100
    return(false_peaks_rate)

def show_false_peaks_rate(bait, hit) : #représentation graphique du LIPR
    bait_b_ions = get_b_ions(bait)
    bait_y_ions = get_y_ions(bait)
    hit_b_ions = get_b_ions(hit)
    hit_y_ions = get_y_ions(hit)
    spc=[]
    vp_masses = []
    fp_masses = []
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                print(elt1,bait_b_ions[elt1],"<--->",elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_b_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                print(elt1,bait_b_ions[elt1],"<--->",elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_y_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                print(elt1,bait_y_ions[elt1],"<--->",elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_b_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                print(elt1,bait_y_ions[elt1],"<--->",elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_y_ions[elt2] :
                    fp_masses.append(elt1)
                else :
                    vp_masses.append(elt1)
    false_peaks = 0
    spc = set(spc)
    for elt in set(fp_masses) :
        if elt not in vp_masses :
            false_peaks += 1
    false_peaks_rate = (false_peaks/len(spc))*100
    return(false_peaks_rate)

def get_spc(bait, hit) :#calcule le SPC entre deux séquences
    bait_b_ions = get_b_ions(bait)
    bait_y_ions = get_y_ions(bait)
    hit_b_ions = get_b_ions(hit)
    hit_y_ions = get_y_ions(hit)
    spc=[]
    wrong_peaks=0
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_b_ions[elt1],"<--->",elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_b_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_b_ions[elt1])
                    #print(elt2,hit_b_ions[elt2])
    for elt1 in bait_b_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_b_ions[elt1],"<--->",elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_b_ions[elt1] != hit_y_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_b_ions[elt1])
                    #print(elt2,hit_y_ions[elt2])
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_b_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_y_ions[elt1],"<--->",elt2,hit_b_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_b_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_y_ions[elt1])
                    #print(elt2,hit_b_ions[elt2])
    for elt1 in bait_y_ions.keys() :
        for elt2 in hit_y_ions.keys() :
            if elt1==elt2 :
                #print(elt1,elt2)
                #print(elt1,bait_y_ions[elt1],"<--->",elt2,hit_y_ions[elt2])
                spc.append(elt1)
                if bait_y_ions[elt1] != hit_y_ions[elt2] :
                    wrong_peaks += 1
                    #print(elt1,bait_y_ions[elt1])
                    #print(elt2,hit_y_ions[elt2])
    spc = set(spc)
    return(len(spc))

#================ Calcul des masses de toutes les séquences possibles de 1 à n résidus ================
#================ Utiles à GreenGlob ================

listMass2 = []
len_to_masses2 = {}
seqLength = 4

for L in range(2, 3) :
    len_mass_list = []
    for subset in itertools.combinations_with_replacement(aaList3, L):
        string = ""
        for letter in list(subset) :
            string += letter
        listMass2.append(get_mass_residue(string))
        len_mass_list.append(get_mass_residue(string))
    len_to_masses2[L] = len_mass_list

listMass2 = set(listMass2)

listMass3 = []
len_to_masses3 = {}

for L in range(2, 4) :
    len_mass_list = []
    for subset in itertools.combinations_with_replacement(aaList3, L):
        string = ""
        for letter in list(subset) :
            string += letter
        #if abs(365.158685473303-get_mass_residue(string)) < 0.01 :
        #    print(string)
        listMass3.append(get_mass_residue(string))
        #if abs(get_mass_residue(string) - 158.068) < 0.01 :
        #    print(string)
        len_mass_list.append(get_mass_residue(string))
    len_to_masses3[L] = len_mass_list

listMass3 = set(listMass3)

listMass4 = []
len_to_masses4 = {}

for L in range(2, 5) :
    len_mass_list = []
    for subset in itertools.combinations_with_replacement(aaList3, L):
        string = ""
        for letter in list(subset) :
            string += letter
        #if abs(156.101111025652-get_mass_residue(string)) < 0.02 :
        #    print(get_mass_residue(string))
        #    print(string)
        listMass4.append(get_mass_residue(string))
        #if abs(get_mass_residue(string) - 158.068) < 0.01 :
        #    print(string)
        len_mass_list.append(get_mass_residue(string))
    len_to_masses4[L] = len_mass_list

listMass4 = set(listMass4)

def main() :

    #for i in range(len(aa_list)) :
    #    print(aa_list[i], mass_list[i])
    
    seq = "TIPYSHR"
    
    dic1 = get_y_ions(seq)
    
    #for elt in dic1.keys() :
    #    print(dic1[elt], elt)
    
    dicb = get_b_ions(seq)
    dicy = get_y_ions(seq)
    
    dicAll = {}
    
    dicAll[mass_dict["H+"]] = "H+"
    
    for elt in dicb.keys() :
        dicAll[elt] = dicb[elt]
    
    for elt in dicy.keys() :
        dicAll[elt] = dicy[elt]
    
    dicAll = dict(sorted(dicAll.items()))
    
    ionChain = ""
    
    with open("ions_bait.csv","w") as bait_file :
        chaine = ""
        chaine2 = ""
        for elt in dicAll.keys() :
            #print(elt, dicAll[elt])
            chaine += (dicAll[elt]+";")
            chaine2 += str(elt)+";"
        chaine = chaine.rstrip(";")
        chaine2 = chaine2.rstrip(";")
        bait_file.write(chaine+"\n"+chaine2)
    
    i = 0
    for elt in dicAll.keys() :
        #print(str(i)+" "+dicAll[elt])
        i += 1
        ionChain += dicAll[elt]+" "
    
    #print(ionChain)
    
    #print(len_to_masses)
    
    #print(show_false_peaks_rate("SQQSGEK","SQQSGEGEK"))
    
    ct = 0
    for elt in listMass3 :
        for elt2 in listMass3 :
            if abs(elt - elt2) < 0.02 :
                #print(elt, elt2)
                ct += 1

    #print(str(ct)+" égalités")

    #114.042927442166 N/GG
    #128.058577506648 Q/GA
    #156.101111025652 R/GV precision près
    #186.07931295157 W/GE/AD précision près
    #255.158291550141 précision près 0/VR
    #255.158291550141 O/GVV/AAI
    print(get_spc("HYIIFCTTVFTIIIISIVIIYCR", "VSGAVSDAIHIIISIIVVQPHM"))

#main()