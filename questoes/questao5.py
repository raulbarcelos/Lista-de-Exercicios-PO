print("********************************")
print("********** QUESTÃO 05 **********")
print("********************************")
print("******** RAUL BARCELOS *********")

arquivo1 = open('grafo.txt', 'r').readlines() # lê o arquivo quebrando em linhas

vertices = 0 #armazena a quantidade de vertices
arestas = 0 #armazena a quantidade de arestas
matriz_txt = [] #armazena matriz lida do arquivo1 com informações do grafo
matriz_adj = [] #armazena matriz adjacente do grafo
vertices_rotulos = [] #armazena os rótulos/nomes/titulos dos vertices
lista_vertices = [] #


def ler_arquivo(arquivo, matriz):
    contador = 0
    for linha in arquivo:
        if (contador == 0):
            vertices_total = int(linha.rstrip())  # se for a primeira linha do arquivo, armazene na variavel vertices
        elif (contador == 1):
            arestas_total = int(linha.rstrip())  # se for a primeira linha do arquivo, armazene na variavel arestas
        else:
            matriz.append(linha.rstrip().split())  # quebra o arquivo em linhas e adiciona à matriz em listas de listas
        contador += 1
    return vertices_total, arestas_total  # retorna o total de vertices e arestas


def remove_duplicados(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def def_rotulos(matriz_txt, lista_vertices):
    for linha in range(len(matriz_txt)):  # para cada linha na matriz
        lista_vertices.append(matriz_txt[linha][0])
    vertices_rotulos = remove_duplicados(lista_vertices)
    return vertices_rotulos


def gerar_matriz_nula(vertices, matriz_adj):
    for i in range(vertices):
        linha_matriz = []
        for j in range(vertices):
            linha_matriz.append(0)
        matriz_adj.append(linha_matriz)


def add_arestas(matriz_adj, matriz_txt, lista_vertices):
    for linha in range(len(lista_vertices)):
        v1 = int(matriz_txt[linha][0])
        v2 = int(matriz_txt[linha][1])
        peso_aresta = matriz_txt[linha][2]
        matriz_adj[v1][v2] = peso_aresta
        matriz_adj[v2][v1] = peso_aresta
        print("v: {} \t→ \tv: {} \t= {}".format(v1, v2, peso_aresta))


def imprimir_matriz(rotulos, num_vertices, matriz_adj):
    print("\t", end="")
    for i in range(num_vertices):
        print(rotulos[i], end="\t")
    print()
    for i in range(num_vertices):
        print(rotulos[i], end="\t")
        for j in range(num_vertices):
            print(matriz_adj[i][j], end="\t")
        print()
    print()


def grau_matriz(rotulos, num_vertices, matriz_adj):

    print("Grau de cada vértice:")
    for i in range(num_vertices):
        grau = 0
        print("v: {} \t→".format(rotulos[i]), end="\t")
        for j in range(num_vertices):
            if matriz_adj[i][j] != 0:
                grau += 1
        print(grau)


    print()


print()
print()
print("Lendo arquivo grafo.txt ... \n")
vertices, arestas = ler_arquivo(arquivo1, matriz_txt)
print("Vértices: [{}]\nArestas: [{}]\n".format(vertices, arestas))
print("Importando dados do arquivo para lista: ")
print(matriz_txt, "\n")

print("Lista de vértices únicos:")
vertices_rotulos = def_rotulos(matriz_txt, lista_vertices)
print(vertices_rotulos, "\n")

print("Gerando matriz adjacente nula:")
gerar_matriz_nula(vertices, matriz_adj)
imprimir_matriz(vertices_rotulos, vertices, matriz_adj)

print("Adicionando arestas com peso...")
add_arestas(matriz_adj, matriz_txt, lista_vertices)

print("\nMatriz de adjacencia do grafo:")
imprimir_matriz(vertices_rotulos, vertices, matriz_adj)

grau_matriz(vertices_rotulos, vertices, matriz_adj)