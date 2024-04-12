class Grafica:
    def __init__(self, n:int, edges:list) -> None:
        self.n = n
        self.lista_adyacencias = [[] for _ in range(n + 1)]
        for edge in edges:
            v1, v2 = edge
            self.lista_adyacencias[v1].append(v2)
            self.lista_adyacencias[v2].append(v1)
        return
    def get_neighbors(self, v)->list:
        return self.lista_adyacencias[v] if v <= self.n else []

    
def read_file():
    with open('C:/Users/alexa/OneDrive/Desktop/practicasCumplejidad/Complejidad/Practica1/inputs/input4.txt', 'r') as f:
        k = int(f.readline().strip())
        n = int(f.readline().strip())        
        linea = f.readline().strip()
        # Extraer las tuplas de la línea
        tuplas = linea.strip()[1:-1].split('), (')
        # Convertir las tuplas a una lista de tuplas
        edges = [tuple(map(int, t.split(','))) for t in tuplas]
        # Imprimir la lista de tuplas obtenida
        print("Lista de tuplas:", edges)
        return k, n, edges
