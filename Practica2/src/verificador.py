from script_read import Grafica, read_certificate, read_file
import sys

def verifica_k_coloracion(g:Grafica, certificado:list):
    """
    Algoritmo que verifica que el certificado sea una solucion
    al problema de k-coloracion, para cada vertice, checa
    todos sus vecinos dentro de el
    Inputs:
    g: grafica de entrada
    certificado: funcion que mapea cada vertice a un color, representada
    por una lista

    Returns:
    True si es una solucion, false de lo contrario
    """
    for i in range(1, g.get_n()):
        for vecino in g.get_neighbors(i):
            if certificado[i - 1] == certificado[vecino - 1]:
                return False
    return True
if __name__ == "__main__":
    k, n, edges = read_file(("./inputs/" + str(sys.argv[1])))
    certificado = read_certificate(("./certificados/" + str(sys.argv[2])))    
    g = Grafica(n, edges)
    if verifica_k_coloracion(g, certificado):
        print("El certificado es una solucion al problema")
    else:
        print("El certificado no es una solucion al problema")
    sys.exit()
