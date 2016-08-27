##Autor Daniel Costa Valerio (WaGjUb)
##Representacao de grafos (lista e matriz)
##Adicionar (V,E)
##Remover (V,E)
##Buscar (V,E)
class aresta(object):
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino

class vertice(object):
    def __init__(self, valor):
        self.valor = valor
        self.listaAdjacencia = []

class grafo(object):
    def __init__(self):
        self.Larestas = []
        self.Lvertices = []

    def adicionarAresta(self, aresta):
        self.Larestas.append(aresta)

    def adicionarVertice(self, vertice): ##
        self.Lvertices.append(vertice)

    def removerVertice(self, vertice): ##
        try:
            self.Lvertices.remove(vertice)
        except ValueError:
            pass
    def removerAresta(self, aresta):
        try:
            self.Larestas.remove(aresta)
        except ValueError:
            pass

    def buscarVertice(self, vertice): ##
        try:
            indice = self.Lvertices.index(vertice)
            return self.Lvertices[indice]
        except ValueError:
            return None

    def buscarAresta(self, aresta):
        try:
            indice = self.Larestas.index(aresta)
            return self.Larestas[indice]
        except ValueError:
            return None

        
def caso_1(g): # adicionar vertice
    valor = input('Digite o valor do vertice: ')
    v = vertice(valor)
    g.adicionarVertice(v)
    
def caso_2(g): # remover vertice
    valor = input('Digite o valor do vertice: ')
    v = vertice(valor)
    g.removerVertice(v)

def caso_3(g): # adicionar aresta
    valor = input('Digite a origem e destino separado por vírgula Ex. o,d: ').split(',')
    if len(valor) == 2:
        print("inseriu")
        a = aresta(valor[0], valor[1])
        g.adicionarAresta(a)

def caso_4(g): # remover aresta
    valor = input('Digite a origem e destino separado por vírgula Ex. o,d: ').split(',')
    if len(valor) != 2:
        a = aresta(valor[0], valor[1])
        g.removerAresta(a)

def caso_5(g): # buscar vertice
    valor = input('Digite o valor do vertice: ')
    v = vertice(valor)
    g.buscarVertice(v)

def caso_6(g): # buscar aresta
    valor = input('Digite a origem e destino separado por vírgula Ex. o,d: ').split(',')
    if len(valor) != 2:
        a = aresta(valor[0], valor[1])
        g.buscarAresta(a)

def caso_7(g): #Imprime grafo    
    print("Vertices: ")
    for v in g.Lvertices:
        print(v.valor)
    print("Arestas: ")
    for a in g.Larestas:
        print("orig: {0} dest: {1}".format(a.origem, a.destino)) #################

def printMenu():
    print("1 - Adicionar vertice",
          "\n2 - Remover vertice",
          "\n3 - Adicionar aresta", 
          "\n4 - Remover aresta",
          "\n5 - Buscar vertice", 
          "\n6 - Buscar aresta",
          "\n7 - Imprimir grafo",
          "\n8 - Sair")

if __name__ == "__main__":
    entrada = 10
    g = grafo()
    mendict = {1: caso_1, 2: caso_2, 3: caso_3, 4: caso_4, 5: caso_5, 6: caso_6, 7: caso_7}
    while True:
        printMenu()
        entrada = int(input("Opção: "))
        if entrada == 8:
            break
        else:
#            try:
            mendict[entrada](g)
#            except:
#                print("Digite uma opção valida!!")


