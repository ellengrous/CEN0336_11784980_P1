#!/usr/bin/env python3

#Importando biblioteca sys
import sys

# Verificando se foram passados todos os argumentos
if len(sys.argv) != 8:
    print("Por favor, forneça 7 argumentos: uma sequência de DNA e seis números inteiros")

# Recebendo a sequência de DNA
sequencia_dna = sys.argv[1]
print(len(sequencia_dna))
# Verificando se o primeiro argumento é uma string
if not sequencia_dna.isalpha():
    print("O primeiro argumento deve ser uma string")
# Recebendo todos os valores a partir do indice 2
coordenadas = sys.argv[2:]

# Navegando por todos os valores na lista de cordenadas
for coordenada in coordenadas:
    # Verificando se todos os valores da lista de coordenadas são inteiros
    if not coordenada.isdigit():
        print("Os argumentos restantes devem ser números inteiros")

    # Verificando se algum dos números da lista é maior que o tamanho da sequência de DNA
    if int(coordenada) > len(sequencia_dna):
        print("Nenhum dos inteiros pode ser maior que o tamanho da sequência de DNA")

# Convertenda a lista de valores de string para inteiro
coordenadas = list(map(int, coordenadas))
# Extraindo as sequências CDS
cds1 = sequencia_dna[coordenadas[0]:coordenadas[1]]
cds2 = sequencia_dna[coordenadas[2]:coordenadas[3]]
cds3 = sequencia_dna[coordenadas[4]:coordenadas[5]]
#

# Verifique se as sequências CDS começam com 'GT' e terminam com 'AG'
if cds1.startswith('GT') and cds1.endswith('AG') and cds2.startswith('GT') and cds2.endswith('AG') and cds3.startswith('GT') and cds3.endswith('AG'):
    # Imprimindo a sequência resultante da junção das CDS 1, CDS 2 e CDS 3
    print(cds1 + cds2 + cds3)
else:
    print(
        f"As sequências: {cds1 + cds2 + cds3} CDS não começam com 'GT' e terminam com 'AG'.")



#Para testar, utilizar a sequência: CGTCGTCGCCGCCGCCGCCATGTCGGGAGGTGGTGTGATGTGTGAGCCGACGAAAAGTAAAAGAAGCGGGGAACAACGACTGCCGCATCTACGTGTAAAAAAACGAAAAAAAAAAAAAAAAAAAA
#E utilizar as coordenadas: n1: 20; n2: 39; n3: 47; n4: 56; n5: 64; n6: 98
