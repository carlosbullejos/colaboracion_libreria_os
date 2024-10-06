import os

#Crear un directorio llamado datos:

os.mkdir('datos')

os.chdir('datos\\') # Cambiando al directorio datos.

print(os.getcwd()) # Mostrando por pantalla el directorio actual en el que estamos trabajando que es datos.

os.makedirs('img', exist_ok=True) # Creación del subdirectorio "img"
os.makedirs('docs', exist_ok=True) # Creación del subdirectorio "docs"
os.makedirs('otros', exist_ok=True) # Creación del subdirectorio "otros"

os.listdir('datos') #Mostrar los subdirectorios creados