import random 

r_range = random.randrange(10,20,2) # (inicio,fim,step)
print(r_range)

r_range = random.randint(10,20)
print(r_range)

r_range = random.uniform(10,20)
print(r_range)

nomes = ['Luiz','Maria','Helena','Joana']
random.shuffle(nomes)
print(nomes)

novos_nomes = random.sample(nomes, k=2)
print(novos_nomes)