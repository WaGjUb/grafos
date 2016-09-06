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
    
    def adicionarAdjacencia(self, destino):
        self.listaAdjacencia.append(destino)

class grafo(object):
    def __init__(self):
        self.Larestas = []
        self.Lvertices = []

    def adicionarAresta(self, aresta):
        vorigem = vertice(aresta.origem)
        vdestino = vertice(aresta.destino)
        origemIndex = self.buscarVertice(vorigem)
#        print(str(origemIndex) + str(self.buscarVertice(vdestino)) + str(self.buscarAresta(aresta)) )
        if ((self.buscarVertice(vdestino) is not False) and (origemIndex is not False) and (self.buscarAresta(aresta) is False)):
            self.Larestas.append(aresta)
            self.Lvertices[origemIndex].adicionarAdjacencia(aresta.destino)
            print("Aresta adicionada")
        else:
            print("Aresta ja existe ou vertices nao existem")

    def adicionarVertice(self, vertice): ##        
        if not self.buscarVertice(vertice):
            self.Lvertices.append(vertice)
        else:
            print("O vertice ja existe!")

    def removerVertice(self, vertice): ##
        try:
            idx = self.buscarVertice(vertice)
            self.Lvertices.pop(idx)
            self.removerArestas(vertice)
            print("Vertice removido!")
        except ValueError:
            pass

    def removerArestas(self, vertice):
        try:
            idx = 0
            for x in range(0, len(self.Larestas)):
                print(idx)
                if ((self.Larestas[idx].origem == vertice.valor) or (self.Larestas[idx].destino == vertice.valor)):
                    self.Larestas.pop(idx)
                else:
                    idx += 1 
        except e:
            pass

    def removerAresta(self, aresta):
        try:
            idx = self.buscarAresta(aresta)
            self.Larestas.pop(idx)
            print("Aresta removida!")
        except ValueError:
            pass

    def buscarVertice(self, vertice): ##
        try:
            indice = [x.valor for x in self.Lvertices].index(vertice.valor)
            return indice
        except ValueError:
            return False

    def buscarAresta(self, aresta):
        try:
            for idx,x in enumerate(self.Larestas):
                if (x.origem == aresta.origem) and (x.destino == aresta.destino):
                    return idx
            return False
        except ValueError:
            return False
        
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
    idx = g.buscarVertice(v)
    if (idx is not False):
            print("O vertice está no grafo")
    else:
            print("O vertice não está no grafo")

def caso_6(g): # buscar aresta
    valor = input('Digite a origem e destino separado por vírgula Ex. o,d: ').split(',')
    if len(valor) != 2:
        a = aresta(valor[0], valor[1])
        idx = g.buscarAresta(a)
    if (idx is not False):
            print("A aresta está no grafo")
    else:
            print("A aresta não está no grafo")

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


