import math
import csv
import os
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))
ruta_estudiantes = os.path.join(base_dir, "lista_adyacencia_estudiantes.csv")

notes = ''
with open(ruta_estudiantes, newline='') as listaAdyacencia:
    data = csv.reader(listaAdyacencia, delimiter=',')
    notes = list(data)

############### CLASE DEL GRAFO ###############    
class Graph:

    def __init__(self, directed: bool = True):
        #self.n = n
        self.directed = True
        self.adyacencia = {}  
        self.adj_matrix = {}  
        #self.edges = []  

    def add_vertex(self, u) -> None:
        if u not in self.adyacencia:
            self.adyacencia[u] = []

    def add_edge(self, origen, destino) -> bool:

        self.add_vertex(origen)
        self.add_vertex(destino)
        self.adyacencia[origen].append(destino)
        self.adj_matrix[(origen, destino)] = 1 

        return True
        pass

    def mostrar_lista(self):
        for nodo, vecinos in self.adyacencia.items():
            print(f"{nodo} -> {vecinos}")

    def degree(self, u) -> int:
        return len(self.adyacencia[u])
        pass
    
    ########### Problema 1 ###########

    def centralidadPorValoresPropios(self, iteraciones_maximas, tolerancia):
        n=100
        x=np.ones(n)/n
        iteracion=0
        converged=False
        while iteracion < iteraciones_maximas and not converged:
            new_x=np.dot(self.adyacencia, x)
            normal=np.linalg.norm(new_x)
            
            
        pass

    
    ########### Problema 2 ###########
    def matriz_de_transición_estocástica(self):
        nodos = sorted(self.adyacencia.keys())
        n = len(nodos)
        idx = {nodo: i for i, nodo in enumerate(nodos)}
        matriz = np.zeros((n, n))

        for origen in nodos:
            destinos = self.adyacencia[origen]
            if destinos:
                prob = 1 / len(destinos)
                for destino in destinos:
                    i = idx[origen]
                    j = idx[destino]
                    matriz[i][j] = prob
            #si un nodo no tiene salidas, se deja la fila en cero

        return nodos, matriz


grafo_estudiantes = Graph()
for origen, destino in notes:
    grafo_estudiantes.add_edge(origen, destino)

############### TALLER ###############   

opcion_menu = 0
while opcion_menu != 3:
    print("------------------------------------------------------------------------")
    print("|        Taller Alg. y Complejidad: Estudiante más famoso                |")
    print("|                                                                        |")
    print("|         1. Centralidad por Valores Propios 🌟                          |")
    print("|         2. PageRank sobre la Red de Estudiantes                         |")
    print("|         3. Salida 🚪                                                   |")
    print("------------------------------------------------------------------------")

    try:
        opcion_menu = int(input("\nIngrese una opción (1-3): "))
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, ingrese un número entre 1 y 3.")
        continue

    if opcion_menu == 1:
        print("\n✨ HAZ ESCOGIDO LA OPCIÓN: Centralidad por Valores Propios ✨\n")

    elif opcion_menu == 2:
        print("\nHAZ ESCOGIDO LA OPCIÓN: PageRank sobre la Red de Estudiantes\n")
       
    elif opcion_menu == 3:
        print("¡Gracias por usar el sistema! 👋")

    else:
        print("⚠️ Opción inválida. Por favor, ingrese un número entre 1 y 3.")