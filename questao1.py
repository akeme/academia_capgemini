'''
# Questão 01

Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
 A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
'''

def escada(tam):
    fim = tam + 1
    for i in range (1,tam):
        a = tam - i
        print(a*' '+ i*'*')
    


aux = int(input( 'Digite a altura/base a sua escada= '))
escada(aux)