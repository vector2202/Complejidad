import random
import sys
import re
from script_read import Grafica
from script_read import read_file
from script_coloracion import _2_coloracion
#En este archivo vamos a implementar, leemos la entrada: k,n,aristsas y construimso la grafica
#A partir de ahi generamos un certificado aleatorio el cual vamos a verificar posteriormente
#Tenemos que leer deentrada el archivo input y en donde lo vamos a guardar.
try:
    k, n, edges = read_file(("./inputs/" + str(sys.argv[1])))
    numCertificado = re.findall(r'\d+', str(sys.argv[2]))

    if ((int)(numCertificado[0]) != 0):

        nuevoCertificado = open("./certificados/certificado"+str(numCertificado[0])+"k"+str(k)+".txt", "w")
        nuevoCertificado.write("(")
        for vertices in range(0,n):
            nuevoCertificado.write(str(random.randrange(1,k+1)))
            if vertices < (n-1):
                nuevoCertificado.write(",")
        nuevoCertificado.write(")")
        nuevoCertificado.close()

    else:
        nuevoCertificado = open("./certificados/certificado"+str(numCertificado[0])+"k"+str(k)+".txt", "w")
        g = Grafica(n, edges)
        coloracion = _2_coloracion(g)
        print(coloracion)
        nuevoCertificado.write("(")
        for i in range(len(coloracion)):
            nuevoCertificado.write(str(coloracion[i]))
            if  i < (n - 1):
                nuevoCertificado.write(",")
        nuevoCertificado.write(")")
        nuevoCertificado.close()
    
except FileNotFoundError:
    print("No se ha generado el certificado")


