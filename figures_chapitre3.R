library(data.table)
library(ggplot2)

links_minscore_60_specfit = fread("links_thr_7_specOMS_shift_60_haschanged_color.txt", h=T, sep = "\t")
links_minscore_60_no_specfit = fread("links_thr_7_specOMS_no_shift_60_r_haschanged_color.txt", h=T, sep = "\t")

#commenter ou décommenter les lignes suivantes pour la Figure 3.11 (20) ou 3.12 (40)
i = 7:20
#i = 7:40

greens = c()
oranges = c()
reds = c()

greensp = c()
orangesp = c()
redsp = c()

for (thr in i) {
  #première ligne pour 3.11
  #seconde pour 3.12
  dataset = links_minscore_60_no_specfit[which(spc_without_specfit>=thr),]
  #dataset = links_minscore_60_specfit[which(spc_with_specfit>=thr),]
  tot = nrow(dataset)
  ngreen = nrow(dataset[which(color=="green"),])
  greens = c(greens, ngreen)
  pgreen = (ngreen/tot)*100
  greensp = c(greensp, pgreen)
  norange = nrow(dataset[which(color=="orange"),])
  oranges = c(oranges, norange)
  porange = (norange/tot)*100
  orangesp = c(orangesp, porange)
  nred = nrow(dataset[which(color=="red"),])
  reds = c(reds, nred)
  pred = (nred/tot)*100
  redsp = c(redsp, pred)
}

data = data.frame(i,greens,oranges,reds)
#commenter ou décommenter les lignes suivantes pour la Figure 3.11 (17) ou 3.12 (21)
fdr_threshold = 17
#fdr_threshold = 21

titre = "Min raw SPC"
#titre = "Min shift SPC"

s = 1.5

ggplot(data=data, aes(x = i))+
  geom_line(aes(y = greensp, colour="Greens"), color = "limegreen", size = s)+
  geom_line(aes(y = orangesp, colour="Oranges"), color = "orange", size = s, linetype = "dotdash")+
  geom_line(aes(y = redsp, colour="Reds"), color = "red", size = s, linetype = "longdash") +
  labs(x = titre, y = "% des PSMs") +
  theme_bw()+ theme(panel.border = element_blank(), panel.grid.major = element_blank(),
                    panel.grid.minor = element_blank(), axis.line = element_line(colour = "black")) +
  geom_vline(xintercept = fdr_threshold, size = 1) + theme(axis.text=element_text(size=14),
                                                axis.title=element_text(size=18))
