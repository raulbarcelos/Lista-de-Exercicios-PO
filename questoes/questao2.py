import random

numeros = list()
define_tamanho = 10

print("********************************")
print("********** QUESTÃO 02 **********")
print("********************************")
print("******** RAUL BARCELOS *********")
print()



def ler_dez_numero(tamanho, lista):
    contador = 0
    for i in range(tamanho):
        i = contador
        verd = True
        while verd:
            print("Digite o {}º número INTEIRO:".format(i+1), end=" ")
            num = input("")
            if not num.lstrip("-").isdigit() and num != "\n":
                print("\nDigite apenas números!\n")
            else:
                verd = False
        numeros.append(int(num))
        contador+=1



    imprimir(tamanho, lista, "digitados")


def gerar_dez_numeros(tamanho, lista):
    for i in range(tamanho):
        numeros.append(int(random.randint(1, 100)))

    imprimir(tamanho, lista, "gerados")
