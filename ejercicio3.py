import os

#Crear un directorio llamado "backup"

os.mkdir('backup')

copiado = os.system('xcopy * backup\\') # Haciendo la copia al directorio backup.

os.chdir('backup') # Cambiar al directorio "backup"

os.rmdir('backup') #Eliminar el directorio y su contenido