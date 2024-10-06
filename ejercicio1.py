import os

#Crear un directorio llamado test:

os.mkdir('test')

comprobacion = os.path.exists('test')
if comprobacion == True: # No incluir nada mas en el IF, es solo para la comprobacion sobre la existencia de la carpeta
    print("El directorio ha sido creado correctamente.")
    
os.chdir('test') # Cambiar al directorio "test"
