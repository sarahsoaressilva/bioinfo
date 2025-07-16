# ==========
# 1st attempt
# Transcribing DNA into RNA 
# Author: Sarah Soares 
# ===========

# name of the txt file
name_file = 'rosalind_rna' + '.txt'

def dna_to_rna(dna): return dna.replace("T", "U") 

def dna_to_rna_2(dna):
    """ Second version without .replace() """
    new = ''
    for i in dna: new += i if dna != "T" else "U"
    return new

with open(name_file, "r") as arquivo:
  dados = arquivo.read()

result = dna_to_rna(dados)

print(f'{result}')
