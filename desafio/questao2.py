'''
Débora se inscreveu em uma rede social para se manter em contato com seus amigos.
A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. 
O site considera uma senha forte quando ela satisfaz os seguintes critérios:
    • Possui no mínimo 6 caracteres.
    • Contém no mínimo 1 digito.
    • Contém no mínimo 1 letra em minúsculo.
    • Contém no mínimo 1 letra em maiúsculo.
    • Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+
Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte. 
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser 
adicionados para uma string qualquer ser considerada segura.
'''

from curses.ascii import isupper


def senha_forte(senha):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0


    for a in senha:
        #Checking for uppercase letter and
        if (a.isupper()) == True:
            count1= 1

        # Checking for lowercase letter and
   
        elif (a.islower()) == True:
            count2= 1
            
        # Checking for a numeric letter and
  
        elif (a.isnumeric()) == True:
            count3= 1

        #checking for a special char
        elif (a.punctuation) == True:
            count4 = 1

    return 6 - (count1+ count2 + count3 + count4)

a = input("Digite uma senha: ")
print(senha_forte(a))
		
