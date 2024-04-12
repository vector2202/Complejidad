import random
import sys
import re
 
try: 
        
    with open(str(sys.argv[1]), "r+") as archivoInput:
        lineas = archivoInput.readlines() 
        k = (int)(lineas[0])
        n = (int)(lineas[1])

        numCertificado = re.findall(r'\d+', str(sys.argv[2]))

        if ((int)(numCertificado[0]) != 0):

            nuevoCertificado = open("../certificados/certificado"+str(numCertificado[0])+"k"+str(k)+".txt", "x")
            nuevoCertificado.write(str(k)+ "\n")
            nuevoCertificado.write(str(n)+ "\n")
            nuevoCertificado.write(str(lineas[2])+"\n")
            nuevoCertificado.write("(")
            for vertices in range(0,n):
                nuevoCertificado.write(str(random.randrange(1,k+1)))
                nuevoCertificado.write(",")

            nuevoCertificado.close()

            with open("../certificados/certificado"+str(numCertificado[0])+"k"+str(k)+".txt", "rb+") as nuevoCertificado: 
                nuevoCertificado.seek(-1, 2) 
                nuevoCertificado.truncate() 
            nuevoCertificado.close()


            with open("../certificados/certificado"+str(numCertificado[0])+"k"+str(k)+".txt", "a") as nuevoCertificado: 
                nuevoCertificado.write(")")
            nuevoCertificado.close()

        else:
            print("cero")

except FileExistsError:
    print("Ya existe un certificado con ese índice")


