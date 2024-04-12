# Verificacion del problema k-coloracion

# Requisitos
Se necesita tener instalado python, para instalarlo:

Para verificar que ya esta instalado:
```
python3 --version
```


Para crear un certificado aleatorio hay que correr el siguiente comando:
```
python3 src/certificado.py inputN.txt certificadoMkX.txt
```

Donde N es el numero de input que decidamos, en el caso de M es el numero de certificado que estamos creando y X es nuestra k que vamos a probar


Para ejecutar el archivo se necesita que los archivos existan, tanto la entrada debe estar localizada en el folder inputs como el certificado en el folder certificado
```
python3 src/verificador.py inputN.txt certificadoMkX.txt
```
Donde N es el numero de input que decidamos, en el caso de M es el numero de certificado que estamos probando y X es nuestra k que vamos a probar si es solucion. Es importante verificar que se esten escribiendo de la misma manera que inputN.txt este con el mismo nombre en la carpeta inputs y certificadoMkX.txt este en la carpeta de certificados

Como nota, input1 es con k=2, input2 es una grafica con k=3 e input3 es una grafica con k=4
