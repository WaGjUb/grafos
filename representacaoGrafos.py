##Autor Daniel Costa Valerio (WaGjUb)
##Representação de grafos (lista e matriz)
##Adicionar (V,E)
##Remover (V,E)
##Buscar (V,E)
class aresta(object):
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino

class vertice(object):
    def __init__(self):
        self.valor = None

class grafo(object):
    def __init__(self):
        self.Larestas = []
        self.Lvertices = [[]]

    def addAresta(self, aresta):
        self.Larestas.append(aresta)

    def addVertice(self, vertice): ##
        self.Lvertices.insert(vertice)

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
        
if __name__ == "__main__":
    entrada = None

    while entrada != 0:
        menu()
        entrada = input(": ")
        if (entrada > 7 || entrada < 0):
            print('\n'*100)
            print("Digite uma opção válida!")
        else:


