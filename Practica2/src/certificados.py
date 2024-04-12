import random

with open("contador.txt", "r+") as contador:
    numCertificado = (int)(contador.read())
    numCertificado = numCertificado + 1
    contador.seek(0)
    contador.write(str(numCertificado))
    contador.truncate()

print(numCertificado)

nuevoCertificado = open("input"+str(numCertificado)+".txt", "x")

nuevoCertificado.write(str(random.randrange(0,4)) + "\n")
numVertices = random.randrange(1,11)
nuevoCertificado.write(str(numVertices) + "\n")

for vertices in range(1,numVertices + 1):
    aristas = random.randrange(0,numVertices+1)
    if(aristas != 0):
        for arista in range(1,aristas):
            nuevoCertificado.write("(" + str(vertices) + "," + str(arista) + ")" + ", ")

nuevoCertificado.close()

with open("input"+str(numCertificado)+".txt", "rb+") as nuevoCertificado: 
    nuevoCertificado.seek(-2, 2) 
    nuevoCertificado.truncate() 