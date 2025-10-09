#Definindo as funcao do programa ,funçoes testáveis 
def soma(a,b):
     return a+b

def mult(a,b):
    return a*b

def div(a,b):
    #tratando excesso
    if a==0 and b==0:
        raise ZeroDivisionError("O numero nao pode ser zero")
    return a/b

if __name__=="__main__":

    nome = input("Digite seu nome: ")
    idade1 = int(input("Digite a primeira idade: "))
    idade2 = int(input("Digite a segunda idade: "))

    #nao é possivel comparar a funcao por isso demos variavel ao resultado de soma

    soma_idade=soma(idade1,idade2)
    

    if soma_idade<15:
        print("Voce nao pode entrar",soma_idade)
    elif soma_idade>=15 and soma_idade<18:
        print("Voce pode entrar mas com um adulto",soma_idade )
    else:
        print("Voce pode entrar já es maior de idade")

    print("O resultado da soma entre as idades é",soma_idade)
    print("O resultado da divisao entre as idades é",div(idade1,idade2))
    print("A multiplicacao desta idade é", mult(idade1,idade2))
