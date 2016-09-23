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
        self.cor = None
        self.distancia = None
        self.timestamp = []    
    def adicionarAdjacencia(self, destino):
        self.listaAdjacencia.append(destino)

class grafo(object):
    def __init__(self):
        self.Larestas = []
        self.Lvertices = []
        self.tempo = 0

    def adicionarAresta(self, aresta):
        destinoIndex = self.buscarVertice(aresta.destino) ### mudar
        origemIndex = g.buscarVertice(aresta.origem)
#       print(str(origemIndex) + str(self.buscarVertice(vdestino)) + str(self.buscarAresta(aresta)) )
        if ((self.buscarAresta(aresta) is False)):
            self.Larestas.append(aresta)
            self.Lvertices[origemIndex].adicionarAdjacencia(self.Lvertices[destinoIndex])
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

    def iniciaBuscaProfundidade(self):
        for i in range(0, len(self.Lvertices)):
            self.Lvertices[i].timestamp = []
            self.Lvertices[i].cor = "branco"
        self.tempo = 0
        for i in range(0, len(self.Lvertices)):
            if self.Lvertices[i].cor == "branco":
                self.buscaProfundidade(self.Lvertices[i])
        self.printaProfundidade()
        

    def buscaProfundidade(self, vertice):
        self.tempo += 1
        idx = self.buscarVertice(vertice)
        self.Lvertices[idx].timestamp.append(self.tempo)
        self.Lvertices[idx].cor = "cinza"
        for v in self.Lvertices[idx].listaAdjacencia:
            if v.cor == "branco":
                self.buscaProfundidade(v)
        self.Lvertices[idx].cor = "preto"
        self.tempo += 1
        self.Lvertices[idx].timestamp.append(self.tempo)

    def printaProfundidade(self):
        for v in self.Lvertices:
            print("Vertice: {0} TSd: {1}  TSf: {2}".format(v.valor, v.timestamp[0], v.timestamp[1]))



    def iniciaLargura(self, verticeini, pai):
        idx = self.buscarVertice(verticeini)
        if idx is not False:
            self.Lvertices[idx].cor = "branco"
        for i in range(0, len(self.Lvertices[idx].listaAdjacencia)):
            if self.Lvertices[idx].listaAdjacencia[i].valor != pai.valor:
                self.iniciaLargura(self.Lvertices[idx].listaAdjacencia[i], self.Lvertices[idx])###############

    def buscaLargura(self, verticeini, verticefim):
        idxini = self.buscarVertice(verticeini)
        idxfim = self.buscarVertice(verticefim)
        self.iniciaLargura(verticeini, verticeini)
        d = 0
        self.Lvertices[idxini].cor = "cinza"
        self.Lvertices[idxini].distancia = d
        cinzas = []
        cinzas.append(self.Lvertices[idxini])
        while len(cinzas) != 0:
                d += 1
                atual = cinzas.pop(0)
                for i in atual.listaAdjacencia:
                    idx = self.buscarVertice(i)
                    if self.Lvertices[idx].cor == "branco":
                        self.Lvertices[idx].cor = "cinza"
                        self.Lvertices[idx].distancia = d
                        if self.Lvertices[idxfim].valor == self.Lvertices[idx].valor:
                            return self.Lvertices[idx].distancia
                        cinzas.append(self.Lvertices[self.buscarVertice(i)])
                idxatual = self.buscarVertice(atual)
                self.Lvertices[idxatual].cor = "preto"
        return -1

    def buscarVertice(self, v): ##
        try:
           # indice = [print(x.valor) for x in self.Lvertices].index(v.valor)
            for indice, x in enumerate(self.Lvertices):
                if (x.valor == v.valor):
                    return indice
            return False
        except ValueError:
            return False

    def buscarAresta(self, aresta):
        try:
            for idx,x in enumerate(self.Larestas):
                if (x.origem.valor == aresta.origem.valor) and (x.destino.valor == aresta.destino.valor):
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
        vorigem = vertice(valor[0])
        vdestino = vertice(valor[1])
        origemIndex = g.buscarVertice(vorigem)
        destinoIndex = g.buscarVertice(vdestino)
        if ((destinoIndex is not False) and (origemIndex is not False) ):
            print("inseriu")
            a = aresta(g.Lvertices[origemIndex], g.Lvertices[destinoIndex])
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
    if len(valor) == 2:
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
        print("orig: {0} dest: {1}".format(a.origem.valor, a.destino.valor)) #################

def caso_8(g): #busca em largura
    valor = input("Digite o valor de origem e o valor de destino separado por vírgula Ex. o,d: ").split(',')
    if len(valor) == 2:
        vo = vertice(valor[0])
        vd = vertice(valor[1])
        distancia = g.buscaLargura(vo, vd)
        if distancia > 0:
            print("a menor distância entre os vertices {0} para {1} é {2}".format(vo.valor, vd.valor, distancia))
        else:
            print("Não há caminho de {0} para {1}".format(vo.valor, vd.valor))
    else:
        print("número de argumentos inválidos!")
       
def caso_9(g): #busca profundidade
    g.iniciaBuscaProfundidade()

def printMenu():
    print("1 - Adicionar vertice",
          "\n2 - Remover vertice",
          "\n3 - Adicionar aresta", 
          "\n4 - Remover aresta",
          "\n5 - Buscar vertice", 
          "\n6 - Buscar aresta",
          "\n7 - Imprimir grafo",
          "\n8 - Busca em largura",
          "\n9 - Busca em profundidade",
          "\n15 - Sair")

if __name__ == "__main__":
    entrada = -1
    g = grafo()
    mendict = {1: caso_1, 2: caso_2, 3: caso_3, 4: caso_4, 5: caso_5, 6: caso_6, 7: caso_7, 8: caso_8, 9: caso_9}
    while True:
        printMenu()
        entrada = int(input("Opção: "))
        if entrada == 15:
            break
        else:
      #      try:
             mendict[entrada](g)
        #    except:
         #       print("Digite uma opção valida!!")
