import os

pasta = "C:/Users/Fujioka/Desktop/GitProjects/aula"
# arquivo = os.listdir(pasta)
arquivo = [file for file in os.listdir(pasta) if 'n' in file]

print(arquivo)





