'''
# Questão 01

Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
 A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
'''
# Imprime uma cadeia de caracters * para apresentar a escada
# Input: tam => inteiro, corresponde a altura/base da escada
def escada(tam):
    for i in range (1,tam):
        a = tam - i
        print(a*' '+ i*'*') #  imprime a caracteres vazio, seguidos de i carecters *  
    

## Chamada da função - o dado será pedido ao usuário
aux = int(input( 'Digite a altura/base a sua escada= '))
escada(aux)