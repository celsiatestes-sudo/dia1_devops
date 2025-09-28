nome = input("Digite seu nome: ")
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

soma=idade1+idade2

if soma<15:
    print("Voce nao pode entrar",soma)
elif soma>=15 and soma<18:
    print("Voce pode entrar mas com um adulto",soma )
else:
    print("Voce pode entrar já es maior de idade")

 #Adicionando funcao multiplicacao
 
def mult():
    return idade1*idade2
print("A multi desta idade é", mult())
 
