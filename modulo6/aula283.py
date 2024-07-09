# C:\Users\f0fp0228\Desktop\Curso DEV\curso_udemy\modulo6

#caminho = r'C:\\Users\\f0fp0228\Desktop\\Curso DEV\\curso_udemy\\modulo6'
#print(caminho)

#os.system('start chrome https://www.google.com/')

import os

caminho = os.path.join('/Users','f0fp0228','Desktop','Curso DEV','curso_udemy','modulo6')
for item in os.listdir(caminho):
    print(item)