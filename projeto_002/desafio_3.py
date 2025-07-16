# ==========
# 1st attempt
# Complementing a Strand of DNA 
# Author: Sarah Soares 
# ===========

# name of the txt file
name_file = 'rosalind_strand_dna' + '.txt'

# [ AAAACCCGGT ]
# [ TTTTGGGCCA ]

def complement_dna(dna_str): 
   # ler ao contrário
   new_str = '' # A -> T, G -> C
   for i in range(-1, - (len(dna_str) + 1) , -1): 
     if dna_str[i] == 'A': new_str += 'T' 
     if dna_str[i] == 'G': new_str += 'C' 
     if dna_str[i] == 'C': new_str += 'G' 
     if dna_str[i] == 'T': new_str += 'A' 
   return new_str

with open(name_file, "r") as arquivo:
  dados = arquivo.read()

result = complement_dna(dados)

print(f'{result}')
