# -*- coding: utf-8 -*-

import networkx as nx
import prefixes_suffixes as ps
import get_mass as mass
import rle as rle
import levenshtein as levenstein
import aa_diversity as diversity

def get_link_type(baitorigin, hitorigin) :
        #abrévation du type de lien
        if baitorigin=="Decoy" and hitorigin=="Decoy" :
            link_type = "de_de"
        elif baitorigin=="Target" and hitorigin=="Target" :
            link_type = "ta_ta"
        elif baitorigin=="Contaminant and Target" and hitorigin=="Contaminant and Target" :
            link_type = "tc_tc"
        elif baitorigin == "Multiple" and hitorigin=="Multiple" :
            link_type = "m_m"
        elif baitorigin=="Contaminant" and hitorigin=="Contaminant" :
            link_type = "co_co"
        elif baitorigin=="Target" and hitorigin=="Decoy" :
            link_type = "ta_de"
        elif baitorigin=="Decoy" and hitorigin=="Target" :
            link_type = "de_ta"
        elif baitorigin=="Contaminant" and hitorigin=="Decoy" :
            link_type = "co_de"
        elif baitorigin=="Decoy" and hitorigin=="Contaminant" :
            link_type = "de_co"
        elif baitorigin=="Multiple" and hitorigin=="Decoy" :
            link_type = "m_de"
        elif baitorigin=="Decoy" and hitorigin=="Multiple" :
            link_type = "de_m"
        elif baitorigin=="Multiple" and hitorigin=="Contaminant and Target" :
            link_type = "m_tc"
        elif baitorigin=="Contaminant and Target" and hitorigin=="Multiple" :
            link_type = "tc_m"
        elif baitorigin=="Target" and hitorigin=="Contaminant and Target" :
            link_type = "ta_tc"
        elif baitorigin=="Contaminant and Target" and hitorigin=="Target" :
            link_type = "tc_ta"
        elif baitorigin=="Multiple" and hitorigin=="Contaminant" :
            link_type = "m_co"
        elif baitorigin=="Contaminant" and hitorigin=="Multiple" :
            link_type = "co_m"
        elif baitorigin=="Decoy" and hitorigin=="Contaminant and Target" :
            link_type = "de_tc"
        elif baitorigin=="Contaminant and Target" and hitorigin=="Decoy" :
            link_type = "tc_de"
        elif baitorigin=="Contaminant" and hitorigin=="Target" :
            link_type = "co_ta"
        elif baitorigin=="Target" and hitorigin=="Contaminant" :
            link_type = "ta_co"
        elif baitorigin=="Contaminant" and hitorigin=="Contaminant and Target" :
            link_type = "co_tc"
        elif baitorigin=="Contaminant and Target" and hitorigin=="Contaminant" :
            link_type = "tc_co"
        elif baitorigin=="Multiple" and hitorigin=="Target" :
            link_type = "m_ta"
        elif baitorigin=="Target" and hitorigin=="Multiple" :
            link_type = "ta_m"
        else :
            print(baitorigin)
            print(hitorigin)
            exit("no link type found !")
        return(link_type)

def is_decoy(baitorigin, hitorigin) :
        #détermine si un PSM est target ou decoy
        if baitorigin=="Decoy" and hitorigin=="Decoy" :
            is_decoy = 0
        elif baitorigin=="Target" and hitorigin=="Target" :
            is_decoy = 0
        elif baitorigin=="Contaminant and Target" and hitorigin=="Contaminant and Target" :
            is_decoy = 0
        elif baitorigin == "Multiple" and hitorigin=="Multiple" :
            is_decoy = 0
        elif baitorigin=="Contaminant" and hitorigin=="Contaminant" :
            is_decoy = 0
        elif baitorigin=="Target" and hitorigin=="Decoy" :
            is_decoy = 1
        elif baitorigin=="Decoy" and hitorigin=="Target" :
            is_decoy = 1
        elif baitorigin=="Contaminant" and hitorigin=="Decoy" :
            is_decoy = 1
        elif baitorigin=="Decoy" and hitorigin=="Contaminant" :
            is_decoy = 1
        elif baitorigin=="Multiple" and hitorigin=="Decoy" :
            is_decoy = 0
        elif baitorigin=="Decoy" and hitorigin=="Multiple" :
            is_decoy = 0
        elif baitorigin=="Multiple" and hitorigin=="Contaminant and Target" :
            is_decoy = 0
        elif baitorigin=="Contaminant and Target" and hitorigin=="Multiple" :
            is_decoy = 0
        elif baitorigin=="Target" and hitorigin=="Contaminant and Target" :
            is_decoy = 0
        elif baitorigin=="Contaminant and Target" and hitorigin=="Target" :
            is_decoy = 0
        elif baitorigin=="Multiple" and hitorigin=="Contaminant" :
            is_decoy = 0
        elif baitorigin=="Contaminant" and hitorigin=="Multiple" :
            is_decoy = 0
        elif baitorigin=="Decoy" and hitorigin=="Contaminant and Target" :
            is_decoy = 1
        elif baitorigin=="Contaminant and Target" and hitorigin=="Decoy" :
            is_decoy = 1
        elif baitorigin=="Contaminant" and hitorigin=="Target" :
            is_decoy = 0
        elif baitorigin=="Target" and hitorigin=="Contaminant" :
            is_decoy = 0
        elif baitorigin=="Contaminant" and hitorigin=="Contaminant and Target" :
            is_decoy = 0
        elif baitorigin=="Contaminant and Target" and hitorigin=="Contaminant" :
            is_decoy = 0
        elif baitorigin=="Multiple" and hitorigin=="Target" :
            is_decoy = 0
        elif baitorigin=="Target" and hitorigin=="Multiple" :
            is_decoy = 0
        else :
            print(baitorigin)
            print(hitorigin)
            exit("is decoy found !")
        return(is_decoy)
    
class Match :
    #ajoute les différentes caractéristiques à l'objet "Match" (le PSM)
    #utilise pour cela les autres codes du répertoire
    def __init__(self):
            pass
    def add_bait(self, bait) :
        self.bait = bait
    def add_hit(self, hit) :
        self.hit = hit
    def add_baitlength(self) :
        self.baitlength = len(self.bait)
    def add_hitlength(self) :
        self.hitlength = len(self.hit)
    def add_baitmass(self) :
        self.baitmass = mass.get_mass(self.bait)
    def add_hitmass(self) :
        self.hitmass = mass.get_mass(self.hit)
    def add_baitorigin(self, origin) :
        self.baitorigin = origin
    def add_hitorigin(self, origin) :
        self.hitorigin = origin
    def add_spc_no_specfit(self, spc) :
        self.spc_no_specfit = spc
    def add_spc_with_specfit(self, spc) :
        self.spc_with_specfit = spc
    def add_delta(self, delta) :
        self.delta = delta
    def add_delta_location(self,location) :
        self.delta_location = location
    def add_psize(self, psize) :
        self.psize = psize
    def add_ssize(self, ssize) :
        self.ssize = ssize
    def add_bait_rle(self) :
        self.bait_rle = self.baitlength/len(rle.rle_encode2(self.bait))
    def add_hit_rle(self) :
        self.hit_rle = self.hitlength/len(rle.rle_encode2(self.hit))
    def add_bait_diversity(self) :
        self.bait_diversity = diversity.get_aa_diversity(self.bait)
    def add_hit_diversity(self) :
        self.hit_diversity = diversity.get_aa_diversity(self.hit)
    def add_levenshtein(self) :
        self.levenshtein = levenstein.levenshtein(self.hit, self.bait)
    def add_bigger_peptide_size(self) :
        if self.hitlength >= self.baitlength :
            self.biggersize = self.hitlength
        else :
            self.biggersize = self.baitlength
    def add_levenshtein_ratio(self) :
        self.ratio = self.levenshtein/self.biggersize
    def add_is_bait_in_hit(self) :
        if self.bait in self.hit :
            self.bait_in_hit = 1
        else :
            self.bait_in_hit = 0
    def add_is_hit_in_bait(self) :
        if self.hit in self.bait :
            self.hit_in_bait = 1
        else :
            self.hit_in_bait = 0
    def add_cutside(self, cutside) :
        if cutside == "Left" or cutside == "Right" :
            self.cutside = cutside
        else :
            self.cutside = "0"
    def add_compco(self, compco) :
        self.compco = compco
    def add_false_peaks_rate(self) :
        #try :
        self.false_peaks_rate = mass.get_false_peaks_rate(self.bait, self.hit)
        #except ZeroDivisionError :
            #self.false_peaks_rate = "null"
    def add_link_type(self) : #one letter code for each type of link ; enable an efficient filter of the graph later
        self.link_type = get_link_type(self.baitorigin, self.hitorigin)
    def add_is_decoy(self) :
        self.is_decoy = is_decoy(self.baitorigin, self.hitorigin)

class Node :
    #ajoute les différentes caractéristiques à l'objet "Node"
    def __init__(self):
            pass
    def add_peptide(self, peptide) :
        self.peptide = peptide
    def add_length(self) :
        self.length = len(self.peptide)
    def add_mass(self) :
        self.mass = mass.get_mass(self.peptide)
    def add_origin(self, origin) :
        self.origin = origin
    def add_tot_degree(self, degree) :
        self.tot_degree = degree
    def add_in_degree(self, degree) :
        self.in_degree = degree
    def add_out_degree(self, degree) :
        self.out_degree = degree
    def add_rle(self) :
        self.rle = self.length/len(rle.rle_encode2(self.peptide))
    def add_aa_diversity(self):
        self.diversity = diversity.get_aa_diversity(self.peptide)
    def add_compco(self, compco) :
        self.compco = compco

def get_multigraph_analysis(input_file, thr, link_types_list) :
    #prend chaque PSM du fichier renvoyé par SpecOMS en entrée
    #calcule et ajoute les différentes infos
    dm_shift_string=input_file.replace(".csv","")
    
    #lit la chaîne "link_types_list" en entrée pour déterminer quels types de liens seront mis dans le fichier de sortie
    link_types_string = ""
    
    if len(link_types_list) == 0 :
        link_types_string = "all_links"
    else :
        for link in link_types_list :
            link_types_string += link+"_"
            
    link_types_string = link_types_string.rstrip("_")
    
    print("Analysis for thr= "+str(thr)+" and link_types = "+link_types_string, flush = True)
    
    print("Graph creation...", flush = True)
    
    G = nx.DiGraph() #création du graphe
    
    matchs = []
    nodes = []
    
    seen = {}
    
    error = 0
    
    with open(input_file,'r') as fichier :
        fichier.readline()
        if len(link_types_list) == 0 :
            #si aucune restriction de "link_types", alors aucune vérification
            for line in fichier :
                line = line.split(";")
                spc_no_specfit = line[2]
                spc_with_specfit = line[3]
                if float(spc_no_specfit) >= thr :
                        bait = line[0]
                        hit = line[1]
                        #print(bait, hit)
                        baitorigin = line[10].replace("\n","")
                        hitorigin = line[9]
                        mass_delta = line[5]
                        location = line[4]
                        cutside = line[7]
                        G.add_edge(bait,hit)
                        #link creation
                        match = Match()
                        match.add_bait(bait)
                        match.add_hit(hit)
                        match.add_spc_no_specfit(spc_no_specfit)
                        match.add_spc_with_specfit(spc_with_specfit)
                        match.add_delta(mass_delta)
                        match.add_delta_location(location)
                        match.add_baitlength()
                        match.add_hitlength()
                        match.add_baitmass()
                        match.add_hitmass()
                        match.add_baitorigin(baitorigin)
                        match.add_hitorigin(hitorigin)
                        match.add_link_type()
                        match.add_is_decoy()
                        match.add_psize(ps.get_shared_prefix_size(bait,hit))
                        match.add_ssize(ps.get_shared_suffix_size(bait,hit))
                        match.add_levenshtein()
                        match.add_bait_rle()
                        match.add_hit_rle()
                        match.add_bait_diversity()
                        match.add_hit_diversity()
                        match.add_is_bait_in_hit()
                        match.add_is_hit_in_bait()
                        match.add_bigger_peptide_size()
                        match.add_levenshtein_ratio()
                        match.add_cutside(cutside)
                        match.add_false_peaks_rate()
                        if match.false_peaks_rate == "null" :
                            exit("erreur LIPR")
                        matchs.append(match)
                        #node creation
                        try :
                            var = seen[bait]
                        except KeyError : 
                            node1 = Node()
                            node1.add_peptide(bait)
                            node1.add_length()
                            node1.add_mass()
                            node1.add_origin(baitorigin)
                            node1.add_rle()
                            node1.add_aa_diversity()
                            nodes.append(node1)
                            seen[bait] = True
                        try :
                            var = seen[hit]
                        except KeyError : 
                            node2 = Node()
                            node2.add_peptide(hit)
                            node2.add_length()
                            node2.add_mass()
                            node2.add_origin(hitorigin)
                            node2.add_rle()
                            node2.add_aa_diversity()
                            nodes.append(node2)
                            seen[hit] = True
        else :#vérification du link_types
            for line in fichier :
                line = line.split(";")
                spc_no_specfit = line[2]
                baitorigin = line[4]
                hitorigin = line[5]
                link_type = get_link_type(baitorigin,hitorigin)
                if float(spc_no_specfit) >= thr and link_type in link_types_list :
                        bait = line[0]
                        hit = line[1]
                        baitorigin = line[4]
                        hitorigin = line[5]
                        mass_delta = line[5]
                        location = line[4]
                        cutside = line[7]
                        G.add_edge(bait,hit)
                        #link creation
                        match = Match()
                        match.add_bait(bait)
                        match.add_hit(hit)
                        match.add_spc_no_specfit(spc_no_specfit)
                        match.add_spc_with_specfit(spc_with_specfit)
                        match.add_delta(mass_delta)
                        match.add_delta_location(location)
                        match.add_baitlength()
                        match.add_hitlength()
                        match.add_baitmass()
                        match.add_hitmass()
                        match.add_baitorigin(baitorigin)
                        match.add_hitorigin(hitorigin)
                        match.add_link_type(link_type)
                        match.add_is_decoy()
                        match.add_psize(ps.get_shared_prefix_size(bait,hit))
                        match.add_ssize(ps.get_shared_suffix_size(bait,hit))
                        match.add_hit_rle()
                        match.add_bait_rle()
                        match.add_bait_diversity()
                        match.add_hit_diversity()
                        match.add_levenshtein()
                        match.add_is_bait_in_hit()
                        match.add_is_hit_in_bait()
                        match.add_bigger_peptide_size()
                        match.add_levenshtein_ratio()
                        match.add_cutside(cutside)
                        match.add_false_peaks_rate()
                        matchs.append(match)
                        #node creation
                        try :
                            var = seen[bait]
                        except KeyError : 
                            node1 = Node()
                            node1.add_peptide(bait)
                            node1.add_length()
                            node1.add_mass()
                            node1.add_origin(baitorigin)
                            node1.add_rle()
                            nodes.append(node1)
                            seen[bait] = True
                        try :
                            var = seen[hit]
                        except KeyError : 
                            node2 = Node()
                            node2.add_peptide(hit)
                            node2.add_length()
                            node2.add_mass()
                            node2.add_origin(hitorigin)
                            node2.add_rle()
                            nodes.append(node2)
                            seen[hit] = True

    print("Graph created.", flush = True)
    print(error)
    #Number of nodes
    nbre_nodes = len(G)     
    print(str(nbre_nodes)+" nodes", flush = True)
    
    #Number of links
    nbre_edges = G.number_of_edges()
    print(str(nbre_edges)+" edges", flush = True)
    
    '''
    #Compute all components
    #ccs = list(nx.connected_component_subgraphs(G, copy = True))
    
    #Number of connected components
    #number_of_cc=len(ccs)
    #print(str(number_of_cc)+" connected components", flush = True)
    
    peptide_to_cc = {}
    
    i = 0
    for cc in ccs :
        i += 1
        for peptide in cc.nodes() :
            peptide_to_cc[peptide] = i
    '''
    #Création et remplissage du fichier "nodes"
    #Description de chaque peptide
    node_file_name = "nodes_thr_"+str(thr)+"_"+dm_shift_string+".txt"
    with open(node_file_name,'w') as node_file :
        node_file.write("Sequence"+"\t"+"Length"+"\t"+"Mass"+"\t"+"Origin"+"\t"+"tot_degree"+"\t"+"in_degree"+"\t"+"out_degree"+"\t"+"rle_potential"+"\t"+"diversity"+"\n")
        for node in nodes :
            node.add_tot_degree(G.degree(node.peptide))
            node.add_in_degree(G.in_degree(node.peptide))
            node.add_out_degree(G.out_degree(node.peptide))
            #node.add_compco(peptide_to_cc[node.peptide])
            node_file.write(str(node.peptide)+"\t"+str(node.length)+"\t"+str(node.mass)+"\t"+str(node.origin)+"\t"+str(node.tot_degree)+"\t"+str(node.in_degree)+"\t"+str(node.out_degree)+"\t"+str(node.rle)+"\t"+str(node.diversity)+"\n")

    print("Nodes file created",flush = True)

    #Création et remplissage du fichier "links"
    #Description de chaque PSM
    link_file_name = "links_thr_"+str(thr)+"_"+dm_shift_string+".txt"
    with open(link_file_name,'w') as link_file :
        link_file.write("bait"+"\t"+"hit"+"\t"+"baitlength"+"\t"+"hitlength"+"\t"+"baitmass"+"\t"+"hitmass"+"\t"+"deltaM"+"\t"+"location"+"\t"+"cutside"+"\t"+"baitorigin"+"\t"+"hitorigin"+"\t"+"spc_without_specfit"+"\t"+"spc_with_specfit"+"\t"+"false_peaks_rate"+"\t"+"prefixe"+"\t"+"suffixe"+"\t"+"levenshtein"+"\t"+"lratio"+"\t"+"rle_potential1"+"\t"+"rle_potential2"+"\t"+"bait_diversity"+"\t"+"hit_diversity"+"\t"+"bait_in_hit"+"\t"+"hit_in_bait"+"\t"+"link_type"+"\t"+"is_decoy"+"\n")
        for match in matchs :
            #match.add_compco(peptide_to_cc[match.bait])
            link_file.write(str(match.bait)+"\t"+str(match.hit)+"\t"+str(match.baitlength)+"\t"+str(match.hitlength)+"\t"+str(match.baitmass)+"\t"+str(match.hitmass)+"\t"+str(match.delta)+"\t"+str(match.delta_location)+"\t"+str(match.cutside)+"\t"+str(match.baitorigin)+"\t"+str(match.hitorigin)+"\t"+str(match.spc_no_specfit)+"\t"+str(match.spc_with_specfit)+"\t"+str(match.false_peaks_rate)+"\t"+str(match.psize)+"\t"+str(match.ssize)+"\t"+str(match.levenshtein)+"\t"+str(match.ratio)+"\t"+str(match.bait_rle)+"\t"+str(match.hit_rle)+"\t"+str(match.bait_diversity)+"\t"+str(match.hit_diversity)+"\t"+str(match.bait_in_hit)+"\t"+str(match.hit_in_bait)+"\t"+str(match.link_type)+"\t"+str(match.is_decoy)+"\n")

    print("Links file created",flush = True)

    #Pure graph characteristics calculation

    #Creation of a file "degrees.txt" to plot node degree distribution in R
    file_name = "degrees_thr_"+str(thr)+"_"+dm_shift_string+".txt"
    with open(file_name,"w") as degrees_file :
        degrees_file.write("degree"+"\n")
        for node in G.nodes() :
            degrees_file.write(str(G.degree(node))+"\n")
    
    print("Degrees file created", flush = True)
    
    '''
    #Creation of a file "connected_components" to plote compco sizes in R
    #file_name = "connected_components_thr_"+str(thr)+"_links_"+link_types_string+".txt"
    #with open(file_name,"w") as compco_file :
    #    compco_file.write("size"+"\n")
    #    for cc in ccs :
    #        compco_file.write(str(cc.number_of_nodes())+"\n")
    
    print("Connected_components file created", flush = True)
    
    #Creation of a file "connected_components" to plote compco sizes in R
    file_name = "connected_components_thr_"+str(thr)+"_links_"+link_types_string+".txt"
    with open(file_name,"w") as compco_file :
        compco_file.write("size"+"\t"+"clustering_coefficient"+"\t"+"diameter"+"\t"+"avg_shortest_path_length"+"\n")
        for cc in ccs :
            compco_file.write(str(cc.number_of_nodes())+"\t"+str(nx.average_clustering(cc))+"\t"+str(nx.diameter(cc))+"\t"+str(nx.average_shortest_path_length(cc))+"\n")
    
    print("Connected_components file created", flush = True)
    
    #Creation of a file "cliques" to plot cliques sizes distribution in R
    file_name = "cliques_thr_"+str(thr)+"_links_"+link_types_string+".txt"
    cliques = nx.find_cliques(G)
    with open(file_name,"w") as cliques_file :
        cliques_file.write("clique_size"+"\n")
        for clique in cliques :
            cliques_file.write(str(len(clique))+"\n")

link_lists = [["de_de"]]
thrs = [i for i in reversed(range(5,11))]

print(thrs)

for link_list in link_lists :
    for thr in thrs :
        get_multigraph_analysis("simplified_links.txt", thr, link_list)
'''

#main
get_multigraph_analysis("specOMS_no_shift_60.csv", 7, [])
get_multigraph_analysis("specOMS_shift_60.csv", 7, [])