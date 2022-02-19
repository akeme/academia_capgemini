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

# Input: senha - string
# Output: how many chars must been add to be a strong password - int

def senha_forte(senha):
    count1 = 0 # Values> 0 or 1 : 0 dont have an uppercase letter - 1 one or more upppercase letter
    count2 = 0 # Values> 0 or 1 : 0 dont have a lowercase letter - 1 one or more lowercase letter
    count3 = 0 # Values> 0 or 1 : 0 dont have a numeric char - 1 one or more numeric char
    count4 = 0 # Values> 0 or 1 : 0 dont have a special char - 1 one or more special char
    passlen = 6 # Password length - given 

    for a in senha:
        #Checking for uppercase letter
        if (a.isupper()) == True:
            count1= 1

        # Checking for lowercase letter
   
        elif (a.islower()) == True:
            count2= 1
            
        # Checking for a numeric 
  
        elif (a.isnumeric()) == True:
            count3= 1

        #checking for a special char
        elif (a.punctuation) == True:
            count4 = 1

    return passlen - (count1+ count2 + count3 + count4)

#Asking for an user input 
a = input("Digite uma senha: ")
print(senha_forte(a))
		
