arq = open("matriz.txt", 'r')
arq2 = open("matriz2.txt", 'r')

print("********************************")
print("********** QUESTÃO 04 **********")
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

def imprime_informacao(titulo):
    print("*************** {} ****************".format(titulo))

mat_a = valores(matriz, matriz_txt, arq)
mat_b = valores(matriz2, matriz2_txt, arq2)
imprime_informacao("MATRIZ A")
imprime_matriz(mat_a)
imprime_informacao("MATRIZ B")
imprime_matriz(mat_b)

arq.close()
arq2.close()


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


resultado_final = soma_matriz(mat_a, mat_b)

def somatorio_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = 0

    for i in range(0, linhas):
        for j in range(0, colunas):
            print("(i:{} j:{}) → {}\t+\t{} =".format(i+1, j+1, matriz[i][j], resultado), end=" {} | \n".format(resultado + int(matriz[i][j])))
            resultado = resultado + int(matriz[i][j])
        print("\n")
    return resultado



imprime_informacao("SOMATÓRIO Mat(A)")
somatorio_a = somatorio_matriz(mat_a)
imprime_informacao("SOMATÓRIO Mat(B)")
somatorio_b = somatorio_matriz(mat_b)

print("O resultado do somatório da Matriz A é: ", somatorio_a)
print("O resultado do somatório da Matriz B é: ", somatorio_b)

print()
imprime_informacao("OBSERVAÇÃO")
print("Aplicando propriedade distributiva realizamos o somatório da Matriz A e B separadamente. Agora podemos multiplicar.")
print()

resultado_somatorio = somatorio_a * somatorio_b
print("O resultado da multiplicação entre os somatórios é:\n→ {} * {}:  =".format(somatorio_a, somatorio_b), resultado_somatorio)

