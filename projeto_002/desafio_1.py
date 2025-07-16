# ==========
# 1st attempt
# Counting DNA Nucleotides
# Author: Sarah Soares 
# ===========

# name of the txt file
name_file = 'rosalind_dna' + '.txt'

# accounting
a = 0
c = 0
g = 0
t = 0

with open(name_file, "r") as arquivo:
  dados = arquivo.read()
  for item in dados:
    if item == 'A':
      a += 1
    elif item == 'C':
      c += 1
    elif item == 'G':
      g += 1
    elif item == 'T':
      t += 1

print(f'{a} {c} {g} {t}')