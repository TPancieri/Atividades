import os

pasta = "C:/Users/Fujioka/Desktop/GitProjects/aula"
arquivo = os.listdir(pasta)

arquivo.sort(reverse=True)

print(arquivo)
