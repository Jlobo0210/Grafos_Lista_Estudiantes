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
        self.adyacencia = {} #Lista de adyacencia
        self.adj_matrix = {} #Mat adyacencia  
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
        nodos = (self.adyacencia.keys())
        n=len(nodos)
        indices = {nodo: i for i, nodo in enumerate(nodos)}
        #inicializamos la matriz de adyacencia
        A = np.zeros((n, n))
        for origen in nodos:
            for destino in self.adyacencia[origen]:
                i = indices[origen]
                j = indices[destino]
                A[i][j] = 1
        
        #inicialozamos el vector de centralidad, las iteraciones y la convergencia
        x=np.ones(n)/n
        iteracion=0
        converged=False
        #iniciamos el bucle de iteraciones para calcular la centralidad teniendo en cuenta la tolerancia
        while iteracion < iteraciones_maximas and not converged:
            new_x=np.dot(A, x)
            normal=np.linalg.norm(new_x)
            
            #normalizamos el vector
            if normal > 0:
                new_x= new_x/normal
            
                
            diferencia= np.linalg.norm(new_x-x) #calculamos la diferencia entre el nuevo vector y el anterior
            if diferencia < tolerancia: # si la diferencia es menor a la tolerancia, se considera que ha convergido
                converged=True
            
            x=new_x #actualizamos el vector de centralidad
            iteracion+=1 #aumentamos el contador de iteraciones
            
        centralidad = [(nodos[i], x[i]) for i in range(n)] #hacemos una tupla con el nombre del nodo y su centralidad
        sorted_centralidad = sorted(centralidad, key=lambda x: x[1], reverse=True) #ordenamos la centralidad de mayor a menor
        return x, iteracion, sorted_centralidad 
            
            
   
        

    
    ########### Problema 2 ###########
    
    def matrizTransicionEstocastica(self, nodos): #cada fila indica las probabilidades de moverse de un estudiante a otro
        n = len(nodos)
        ind = {} #para luego construir la matriz, se une cada nodo con un indice del enumerate
        for i, nodo in enumerate(nodos):
            ind[nodo] = i

        matriz = np.zeros((n, n))

        for origen in nodos:
            destinos = self.adyacencia[origen]
            if destinos: #si tiene destinos, se calcula la prob, sino se quedan los 0
                for destino in destinos:
                    i, j = ind[origen], ind[destino]
                    matriz[i][j] = 1/len(destinos) #Mat estocástica

        return matriz

    def pagerank(self, nodos, iteraciones_maximas):
        n = len(nodos)
        M = self.matrizTransicionEstocastica(nodos)

        PR = np.ones(n) / n  #se utiliza un vector de importancia inicial (1/n elementos), pagerank
        teleport = np.ones(n) / n
        iteracion = 0
        
        while iteracion < iteraciones_maximas:
            PR = 0.85 * np.dot(M.T, PR) + (1 - 0.85) * teleport
            iteracion += 1
        
        ranking = list(zip(nodos, PR)) #una lista de tuplas de estudiantes con su puntaje de pagerank
        ranking.sort(key=lambda x: x[1], reverse=True) #reverse es que ordene de mayor a menor

        return ranking

grafo_estudiantes = Graph()
for origen, destino in notes:
    grafo_estudiantes.add_edge(origen, destino)

estudiantes = sorted(grafo_estudiantes.adyacencia.keys()) #nodos del dicc

############### TALLER ###############   

opcion_menu = 0
while opcion_menu != 3:
    print("------------------------------------------------------------------------")
    print("|        Taller Alg. y Complejidad: Estudiante más famoso                |")
    print("|                                                                        |")
    print("|         1. Centralidad por Valores Propios 🌟                          |")
    print("|         2. PageRank sobre la Red de Estudiantes 🔝                     |")
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
        ranking = grafo_estudiantes.pagerank(estudiantes, 5)

        print("🔝 Ranking de estudiantes por PageRank:\n")
        for i, (nombre, puntaje) in enumerate(ranking, 1):
            print(f"{i}. {nombre}: {round(puntaje, 4)}")
        print("\n")
    elif opcion_menu == 3:
        print("¡Gracias por usar el sistema! 👋")

    else:
        print("⚠️ Opción inválida. Por favor, ingrese un número entre 1 y 3.")