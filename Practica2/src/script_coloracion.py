from script_read import Grafica
import random
import sys
def _2_coloracion(g:Grafica):
    """
    Funcion que resuelve el problema de 2 coloracion, devuelve la lista con la solucion o dice que no es coloreable
    Args:
    g: grafica que vamos a colorear
    Returns:
    Lista que representa la coloracion
    """
    queue = [random.randint(1, g.n)]
    colors = [0] * (g.n + 1)
    while(queue.__len__() > 0):
        v = queue.pop(0)
        neighbors = g.get_neighbors(v)
        color = 1 if colors[v] == 2 else 2
        for neighbor in neighbors:
            if colors[neighbor] == 0:
                colors[neighbor] = color
                queue.append(neighbor)
            elif colors[neighbor] != color:
                print("Grafica no 2-colorable")
                sys.exit()
    return colors[1:]
    
