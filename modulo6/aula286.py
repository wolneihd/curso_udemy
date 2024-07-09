import os
import shutil

home = os.path.expanduser('~')
print(home)

desktop = os.path.join(home,'Desktop')
print(desktop)

pasta_original = os.path.join(home, desktop, 'Curso DEV', 'curso_udemy', 'varias_aulas')
print(pasta_original)

# criar nova pasta
# nova_pasta = os.path.join(pasta_original, 'new_directory')
# os.makedirs(nova_pasta, exist_ok=True); print('pasta criada!')

for root, dirs, files in os.walk(pasta_original):
    for file in files:
        print(file)
