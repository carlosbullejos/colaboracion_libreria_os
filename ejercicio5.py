import os

#Crear un directorio llamado datos:

os.mkdir('datos')
os.chdir('datos\\') # Cambiando al directorio datos.
print(os.getcwd()) # Mostrando por pantalla el directorio actual en el que estamos trabajando que es datos.
