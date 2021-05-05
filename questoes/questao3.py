arq = open("matriz.txt", 'r')
arq2 = open("matriz2.txt", 'r')

print("********************************")
print("********** QUESTÃO 03 **********")
print("********************************")
print("******** RAUL BARCELOS *********")
print()

matriz_txt = []
matriz2_txt = []

matriz = []
matriz2 = []


# função para importar valores do arquivo de texto
print("Importando arquivos txt e salvando em matriz...\n")
def valores(matriz, matriz_txt, arquivo):
    matriz_txt = arquivo.readlines()  # retorna o arquivo em forma de linha em listas, cada linha vira um elemento desse vetor
    for i in range(len(matriz_txt)):
        matriz.append(matriz_txt[i].split())
    return matriz


# função para imprimir matriz
def imprime_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print()


# função para imprimir os asteríscos
def imprime_informacao(titulo):
    print("*************** {} ****************".format(titulo))


# função para criar matrizes
def criar_matriz(linhas, colunas, valor):
    nova_matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor)
        nova_matriz.append(linha)
    return nova_matriz


# função para somar as matrizes
def soma_matriz(matriz_a, matriz_b):
    linhas = len(matriz_a)
    colunas = len(matriz_a[0])
    resultado = criar_matriz(linhas, colunas, 0)

    for linha in range(0, linhas):
        for coluna in range(0, colunas):
            resultado[linha][coluna] = int(matriz_a[linha][coluna]) + int(matriz_b[linha][coluna])
    return resultado


mat_a = valores(matriz, matriz_txt, arq)
mat_b = valores(matriz2, matriz2_txt, arq2)
imprime_informacao("MATRIZ A")
imprime_matriz(mat_a)
imprime_informacao("MATRIZ B")
imprime_matriz(mat_b)

arq.close()
arq2.close()
