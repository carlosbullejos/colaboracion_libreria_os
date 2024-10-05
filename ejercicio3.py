import os

#Crear un directorio llamado "backup"

os.mkdir('backup')
copiado = os.system('xcopy * backup\\') # Haciendo la copia al directorio backup.

