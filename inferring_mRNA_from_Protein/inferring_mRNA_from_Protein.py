dict = {'F': ['UUU', 'UUC'],
 'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'],
 'I': ['AUU', 'AUC', 'AUA'],
 'V': ['GUU', 'GUC', 'GUA', 'GUG'],
 'M': ['AUG'],
 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
 'P': ['CCU', 'CCC', 'CCA', 'CCG'],
 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
 'A': ['GCU', 'GCC', 'GCA', 'GCG'],
 'Y': ['UAU', 'UAC'],
 'H': ['CAU', 'CAC'],
 'N': ['AAU', 'AAC'],
 'D': ['GAU', 'GAC'],
 'Stop': ['UAA', 'UAG', 'UGA'],
 'Q': ['CAA', 'CAG'],
 'K': ['AAA', 'AAG'],
 'E': ['GAA', 'GAG'],
 'C': ['UGU', 'UGC'],
 'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
 'G': ['GGU', 'GGC', 'GGA', 'GGG'],
 'W': ['UGG']}

protein_string = input()
all_mRNA = 1
for i in protein_string:
    all_mRNA *= len(dict[i])

all_mRNA *= len(dict['Stop'])
print(all_mRNA%1000000)
