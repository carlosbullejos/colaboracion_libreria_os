import os

#Crear un directorio llamado "backup"

os.mkdir('backup')
os.system('xcopy * backup\\')