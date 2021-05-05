import random

numeros = list()
define_tamanho = 10

print("********************************")
print("********** QUESTÃO 02 **********")
print("********************************")
print("******** RAUL BARCELOS *********")
print()


def pagina_inicial(tamanho, lista):
    lista.clear()

    opcao_str = input("1 → Digitar números \n2 → Gerar aleatóriamente \n0 → Sair da questão\nSelecione a opção:")

    if not opcao_str.isdigit():
        print("\nOpção inexistente. Tente novamente!\n")
        pagina_inicial(tamanho, lista)

    opcao = int(opcao_str)
    print()
    if opcao == 1:
        ler_dez_numero(tamanho, lista)
    elif opcao == 2:
        gerar_dez_numeros(tamanho, lista)
    elif opcao == 0:
        print("Saindo da questão!")
        return
    else:
        print("Opção incorreta! Tente novamente.", end="\n\n")
        pagina_inicial(tamanho, lista)


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


def imprimir(tamanho, lista, forma):
    print("|-------------------------------------------|")
    print("Os números {} foram:".format(forma))
    print("→", lista, end="\n\n")
    print("••• O maior valor é", max(lista))
    print("••• O menor valor é", min(lista))
    print("••• A média é", sum(lista) / tamanho, end="\n\n")
    lista.sort()
    print("Ordem crescente:")
    print("→", lista)
    print("Ordem decrescente:")
    lista.reverse()
    print("→", lista)
    print("|-------------------------------------------|", end="\n\n")
    pagina_inicial(tamanho, lista)


pagina_inicial(define_tamanho, numeros)