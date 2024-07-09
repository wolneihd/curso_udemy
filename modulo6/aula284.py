import os
from itertools import count

caminho = os.path.join('/Users','f0fp0228','Desktop','Curso DEV','curso_udemy','modulo6')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, root)
    for dir_ in dirs:
        print('  ', the_counter, dir_)
    for file_ in files:
        print('  ', the_counter, file_)

# os.unlink(caminho)