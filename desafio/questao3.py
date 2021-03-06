'''
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem 
ser realocadas para formar a outra palavra. 
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que 
são anagramas.
'''

# Função principal 
# Compara as substrings para ver se existe uma substring reversa igual 
# input: palavra - string
# output: quantidade de "anagramas" - inteiro


def anagrama(palavra):
    qtd = 0
    lista_substrings = substrings(palavra)
    for i in range(0,len(lista_substrings)):
        for j in range(1,len(lista_substrings)):
            #print(i,lista_substrings[i],j, lista_substrings[j])
            if (i<j):
                if lista_substrings[i] == lista_substrings[j] [::-1]:
                    #print(i,lista_substrings[i],j, lista_substrings[j] [::-1])
                    qtd +=1
    return qtd
    


## Função auxiliar - monta todas as substrings de uma palavra
# Input: String 
# Output: vetor de strings com todas as substrings da palavra

def substrings(palavra):
    aux = []
    for i in range(0, len(palavra)+1):
        for j in range(len(palavra),0,-1):
            if (i!=j) and (i < j):
                aux.append(palavra[i:j])
    return aux


# Chamada da função
a =  input("digite a palavra a ser analisada: ")
print(anagrama(a))