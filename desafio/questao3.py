'''
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem 
ser realocadas para formar a outra palavra. 
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que 
são anagramas.
'''

from operator import sub


def anagrama(palavra):
    qtd = 0
    lista_substrings = substrings(palavra)
    for i in range(0,len(lista_substrings)):
        for j in range(1,len(lista_substrings)):
            print(i,lista_substrings[i],j, lista_substrings[j])
            if (i!=j):
                if lista_substrings[i] == lista_substrings[j] [::-1]:
                    print(i,lista_substrings[i],j, lista_substrings[j] [::-1])
                    qtd +=1
    return qtd
    



def substrings(palavra):
    aux = []
    for i in range(0, len(palavra)+1):
        for j in range(len(palavra),0,-1):
            if (i!=j) and (i < j):
                aux.append(palavra[i:j])
    return aux



print(anagrama("ifailuhkqq"))