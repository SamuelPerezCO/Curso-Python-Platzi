import os

#Obtener el directorio actual
'''cwd = os.getcwd()
print(f"Directorio de trabajo actual {cwd}")'''

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: " , txt_files)

os.rename('caperucita.txt','cuento.txt')
print('Archivo renombrado', txt_files)

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: " , txt_files)
