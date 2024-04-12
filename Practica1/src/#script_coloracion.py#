from script_read import Grafica, read_file
import random
import sys
def _2_coloracion(g:Grafica):
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
        
    print("Grafica 2 coloreable")
    for i in range(1, colors.__len__()):
        print(f"Para v={i}, su color es:{colors[i]}")
    return

if __name__ == "__main__":
    k, n, edges = read_file()
    if k > 2:
        print(f"El problema de la {k}-coloracion es NP")
        sys.exit()
    g = Grafica(n, edges)
    _2_coloracion(g)
    
