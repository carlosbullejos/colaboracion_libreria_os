import os

#Renombre el archivo "archivo.txt":

os.system('copy archivo.txt copia.txt')

listar = os.listdir('backup\\') #Listando el directorio backup
print(listar) # Mostrando por pantalla el listado del directorio.

os.rename('copia.txt', 'movido.txt') # Script para mover archivo