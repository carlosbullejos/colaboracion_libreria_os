import os

# Eliminar el directorio test:

os.rmdir('test')

archivo_inicializado = open('archivo.txt', 'w') # Inicializando archivo vacio.

os.rename('archivo.txt', 'archivo_renombrado.txt') # Renombrar archivo.txt