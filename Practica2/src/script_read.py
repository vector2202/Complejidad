import sys


class Grafica:
    """
    Clase la cual nos premite representar una grafica
    """
    def __init__(self, n:int, edges:list) -> None:
        """
        Constructor de la grafica
        Params:
        n: numero de vertices de la grafica
        Edges: lista de aristas de la grafica
        """
        self.n = n
        self.lista_adyacencias = [[] for _ in range(n + 1)]
        for edge in edges:
            v1, v2 = edge
            self.lista_adyacencias[v1].append(v2)
            self.lista_adyacencias[v2].append(v1)
        return
    def get_neighbors(self, v)->list:
        return self.lista_adyacencias[v] if v <= self.n else []
    def get_n(self)->int:
        return self.n
        
def read_file(path):
    """
    Funcion que nos permite leer de un archivo que contiene la entrada del
    problema de k-coloracion, la k, la n (numero de vertices) y las aristas
    de la grafica
    Args:
    paht: ruta del archivo a leer la entrada de la grafica y k
    Returns:
    k: el numero de colores maximo permitido para colorear la grafica
    n: el numero de vertices de la grafica
    edges: la lista de tuplas que representan las aristas de la grafica
    """
    try:
        with open(path, 'r+') as f:
            k = int(f.readline().strip())
            n = int(f.readline().strip())        
            linea = f.readline().strip()
            # Extraer las tuplas de la línea
            tuplas = linea.strip()[1:-1].split('), (')
            # Convertir las tuplas a una lista de tuplas
            edges = [tuple(map(int, t.split(','))) for t in tuplas]
            #print("Lista de tuplas:", edges)
            return k, n, edges
    except FileNotFoundError as e:
        print("No existe ese input")
        sys.exit()

def read_certificate(path):
    """
    Funcion que nos permite leer un certificado
    Args:
    path: ruta del certificado
    Returns:
    certificado: lista que representa para el vertice i, l[i] el color
    asignado al vertice
    """
    try:
        with open(path, 'r+') as f:
            certificado = f.readline().strip()
            certificado = certificado.strip('()').split(',')
            certificado = [int(elemento) for elemento in certificado]
            print("Certificado: ", certificado)
            return certificado
    except FileNotFoundError as e:
        print("No se ha generado el certificado")
        sys.exit()

