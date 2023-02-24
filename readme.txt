Codes thèse Albane

De nombreux codes utilisent le fichier "get_mass.py", dans lequel sont stockées les masses des résidus (en Da), et qui a des fonctions pour calculer la masse des peptides entiers, des ions b et des ions y. D'autres fonctions utiles y sont présentes et sont commentées, comme les fonctions liées au LIPR.

Chapitre 3 (dossier "SpecOMS_chap3") :

- SpecOMS
	- Contient SpecOMS et dans "source", contient le protéome humain et les scripts pour
	    - Ne sélectionner que les séquences "protein_coding"
	    - Retirer les peptides tryptiques contenant "*" (acide aminé inconnu)
Autres fichiers :
- Traitement des résultats SpecOMS
	- Graphe
		- "specOMS_shift_all_solutions.csv" contient tous les hits pour un bait avec un seuil de 7
		- "graphe.py" le prend en entrée et :
		    - Crée l'histogramme de degrés Figure 3.5
		    - Crée le fichier "graphe.gexf", lisible par Gephi ; il faut alors sélectionner les noeuds selon le degré et le SPC
		    - On peut ensuite colorer les noeuds selon l'origine target/decoy et lancer la spacialisation fruchterman reingold, que l'on peut enregistrer sous "graphe.gephi". On peut alors produire les Figures 3.6 à 3.8
	- Comparaison des stratégies
		- LIPR
		- RLE
		- Diversité en résidus
			- Ces derniers sont calculés par le fichier "multigraph.py"
				- Besoin pour cela de
					- get_mass.py
					- prefixes_suffixes.py
					    - Calcule les plus longs préfixes et suffixes ; pas de résultats très intéressants alors je n'en ai pas parlé dans le manuscrit
					- rle.py
						- Fonctions pour compresser une chaîne de caractères par RLE
					- levenshtein.py
						- Calcule la distance de Levenshtein entre deux chaînes de caractères ; utilisé plus tard dans la classification couleurs
					- aa_diversity.py
						- Fait une chaîne de caractères avec les caractères non redondants d'une chaîne de caractères "peptide" et divise la taille de celle-ci par la taille du peptide, afin de calculer ce que j'ai appelé la "diversité en résidus" dans le manuscrit
				- Prend en entrée les fichiers résultats de SpecOMS "specOMS_no_shift_60.csv" et "specOMS_shift_60.csv"
				- Renvoie en sortie les fichiers "links_thr_7_specOMS_no_shift_60.txt" et "links_thr_7_specOMS_shift_60.txt"
				- Le shift SPC n'est pas présent dans le fichier "links_thr_7_specOMS_no_shift_60.txt" (puisque shift est désactivé, shift SPC = raw SPC), cependant, il est utile au calcul des couleurs, alors on utilise le script "realign_shift_false.py" afin de produire "links_thr_7_specOMS_no_shift_60_r.txt" dans lequel le shift SPC est ajouté grâce au fichier "specOMS_shift_all_solutions"
				- Le script "has_changed.py" prend en entrée "links_thr_7_specOMS_no_shift_60_r.txt" et "links_thr_7_specOMS_shift_60.txt" afin de produire les équivalents avec la colonne "has_changed" ; cette colonne indique, pour chaque bait, si le hit est le même (0) ou différent (1) entre les deux stratégies (afin de pouvoir retrouver les jeux SS1 et SS2)
				- Les fichiers produits permettent donc de :
					- Calculer les couleurs et le LIPR pour PSM1/PSM2 et SS1/SS2 (auquel cas on filtre sur "has_changed")
					- Ajouter une colonne "color", ce qui permettra de produire les courbes 3.11 et 3.12 à l'aide du script R "figures_chapitre3.R"
					- Calculer le FDR selon le seuil pour PSM1 et PSM2
					- Calculer les courbes RLE, diversité et LIPR selon l'origine target ou decoy des peptides (Figures 3.13 à 3.17)
					- Attention selon le jeu de donné traité de modifier les seuils (jusqu'à 20 ou 40), le score (spc with/without specfit), has_changed si besoin
						- Pour "courbes_rle_target_decoy.py", il faut également modifier la variable à prendre en compte (RLE et diversité selon besoin)

======================================================================================================================================================

Chapitre 4 :

- SpecGlob
    - 

- Comparaison MODPlus
	- Dominique a produit les fichiers "[...]HomoSapiens_[ND/SCT]_SpecOMS.csv", résultats de l'exécution de SpecOMS avec 50 000 peptides

===================================

Représentation des spectres

- Code R pour représenter les spectres théoriques