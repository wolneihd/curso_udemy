"""
DocString - nome do comentário longo ---> 3" ou 3'
Todo conteúdo do curso de Python do Udemy
Focar 1h do dia para o curso.
"""

# Aula 18
print(12, 34, 56, sep='-', end='##')
print(12, 34, 56, sep="-", end='\r\n')

# Aula 19
print(1234)
print('Wolnei')
print("wolnei")
print("wolnei \"wolnei\"")
print(r"wolnei \"wolnei\"")
print('wolnei "wolnei"')

# Aula 20
print(11)
print(-11)
print(1.1)
print(type(1))
print(type('wolnei'))

# Aula 21
print(10==10)
print(type(10==10))

# Aula 22
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1, type(float('1') + 1))
print(bool(''))
print(bool('x'))
print(str(11) + 'b')

# Aula 23
nome_completo = 'Wolnei Hellmann Dircksen'
print(nome_completo)

nome = 'Wolnei'
idade = 32
maior_de_idade = idade >= 18
print('Nome:', nome, 'idade:', idade, 'é maior?', maior_de_idade)

# Aula 24
nome = 'Wolnei'
sobrenome = 'Hellmann Dircksen'
ano_nascimento = 1991
idade = 2024-ano_nascimento
maior_de_idade = idade >= 18
altura_metros = 1.78

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)

# Aula 26
adicao = 10 + 10
print(adicao)

subtracao = 10 - 5
print(subtracao)

multiplicacao = 10*10
print(multiplicacao)

divisao = 10 / 2.2 #float
print(divisao)

divisao_inteira = 10//2.2 #corta fora o que tem depois da virgula
print(divisao_inteira)

exponeciacao = 2 ** 10
print(exponeciacao)

modulo = 55 % 2 #resto da divisão
print(modulo)

print(10%8 == 0) #10 não é multiplo de 0. Resto da conta é diferente de zero.

# Aula 27
concatenar = 'A' + 'B' + 'C'
print(concatenar)

repetir = 'A' * 10
repetir2 = 3 * 'A'
print(repetir)
print(repetir2)

# Aula 28
conta1 = 1 + 1 ** 5 + 5
print(conta1)

# Aula 29
nome = 'Wolnei'
altura = 1.78
peso = 63.2
print(nome, 'tem IMC de', peso/(altura**2))

# Aula 31
nome = 'Wolnei'
altura = 1.78
peso = 63.2
imc = peso/(altura**2)
linha_1 = f'{nome} tem de {altura:.2f} de altura e IMC de {imc:.2f}'
print(linha_1)

valor = 100000.4
print(f'{valor:,.2f}') #insere um ponto entre os milhares.

# Aula 32
a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
formato1 = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
formato2 = 'a={0} a={0} a={0} b={1} c={2:.2f}'.format(a, b, c)
formato3 = 'a={}\rb={}\rc={}'.format(a, b, c)
print(formato)
print(formato1)
print(formato2)
print(formato3)

# Aula 33
nome=input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite um número: '))
print(f'A soma dos números é {numero_1 + numero_2}')

# Aula 34
# if elif else
entrada = input('Você quer "entrar" ou "sair"? ')
if entrada == 'entrar':
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Você digitou nem entrar, nem sair!')

# Aula 35
condicao = True
if condicao:
    print('Este é o código do If')
elif condicao == False:
    pass
else:
    ...
print('Fora do if!')

# Aula 36
# Breaking point
 
# Aula 37
# != diferente
# Todos True para mostrar como funcionam.
print(2>1)
print(2>=2)
print(1<2)
print(1<=2)
print(2<=2)
print('a'=='a')
print('a'!='b')

# Aula 38
primeiro_valor = input('Digite um 1° valor: ')
segundo_valor = input('Digite um 2° valor: ')

if primeiro_valor == segundo_valor:
    print('Os valores são iguais!')
elif primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}!')
else:
    print(f'{primeiro_valor} é menor que {segundo_valor}!')

# Aula 40
entrada = input('[E] Entrar [S] Sair: ')
senha = input('Senha: ')
senha_resposta= ('1234')
if entrada == 'E' and senha == senha_resposta:
    print('Entrar!')
else:
    print('Não permitido!')
    
print(True and False and True) #só avalia té o false - avaliação de curto circuito.
print(bool(0)) #false

# Aula 41
entrada = input('[E] Entrar [S] Sair: ')
senha = input('Senha: ')
senha_resposta= ('1234')
if (entrada == 'E' or entrada == 'e') and senha == senha_resposta:
    print('Entrar!')
else:
    print('Não permitido!')

print(False or False or True) #True

# Aula 42
senha = input('Senha: ')
if senha != '123456':
    print('Senha incorreta!')

senha = input('Senha: ')
if not senha: #se estiver vazio, será False, mas será invertido para TRUE com o is not. 
    print('Você digitou nada!')
    
# Aula 43
nome = 'wolnei'
print(nome[2]) #L
print('o' in nome)
print('z' in nome)
print('a' is not nome)

# Aula 44
# s string, d/i int, f float, x/X Hexadecimal
nome = 'Luiz'
preco = 1000.95265418
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexidecimal de %d é %08x' % (1500,1500))

# Aula 45
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:$^10}')
print(f'{1000.5418941654:+,.2f}')

# Aula 46 [i:f:p]
variavel = 'Olá mundo'
print(variavel[4:8])
print(variavel[4:])
print(variavel[:4])
print(len(variavel))

# Aula 47 
nome = input('Qual o seu nome? ' )

print(10*'-')

print(f'Seu nome é {nome}.')

#print(f'Seu nome invertido é {nome[::-1]}')
indice = len(nome)-1
nome_invertido = ''
for letra in nome:
    letra_invertida = nome[indice]
    nome_invertido = nome_invertido + letra_invertida
    indice=indice-1
print(f'Seu nome invertido é {nome_invertido}.')

if ' ' in nome:
    print(f'Seu nome {nome} contei espaços!')
else:   
    print(f'Seu nome {nome} NÃO contei espaços!')
    
print(f'Seu nome contêm {len(nome)} letras.')

#print(f'A última letra do seu nome é {nome[-1]}')
ult_letra = len(nome) -1
print(f'A última letra do seu nome é {nome[ult_letra]}.')

# Aula 49
numero = input('Dobrar o número: ')
try:
    numero = float(numero)
    print(f'O dobro de {numero} é {numero*2}')
except:
    print(f'"{numero}" não é um número!')
    
# Aula 50
"""
CONSTANTE --> VALOR_1 = 10
Evitar excesso de if
Evitar complexidade.
"""

# Aula 53
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo!')
else:
    print('Não faça algo!')
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

# Aula 54
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número: ')

try:
    teste = (float(num) % 2) == 0
    if teste:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é impar!')
except:
    print('Você digitou algo que não era um número!')
    
    
num = input('Digite um número: ')
verificacao = (num % 2)
print(verificacao)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Insira a sua hora: ')

try: 
    hora = int(hora)
    if hora >= 0 and hora <=11:
        print('Bom dia!')
    elif hora >= 12 and hora <=17:
        print('Boa tarde!')
    elif hora >=18 and hora <=23:
        print('Boa noite!')
    else:
        print('Você inseriu um horário maior que o permitido!')
except:
    print('Você inseriu valor não permitido!')
    
# Aula 58
string = 'wolnei'
string_nova = f'{string[:3]} N {string[4:]}'
print(string_nova)
print(string.zfill(10))

# Aula 59

a = int(0)
while a <= 10:
    print(a)
    a = a + 1
    
condicao = True
while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')
    if nome == 'wolnei':
        break
        
# Aula 60
contador = 0
while contador <= 10:
    print(contador)
    contador = contador + 1
    
# Aula 61
contador = 0
while contador <= 10:
    print(contador)
    contador += 1 #contador = contador + 1 ==> = += -= *= /= //= **= %=
    
# Aula 62
contador = int(0)
while contador <= 10:
    contador += 1
    if contador == 4:
        print('- Continue vai pular o 4')
        continue
    print(contador)
    
# Aula 63
qtd_linhas = 5
qtd_colunas = 5
linha = 1
coluna = 1

while linha <= qtd_linhas:
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna +=1        
    linha +=1

# Aula 64
nome = input('Digite seu nome: ')
indice = 0
string_nova = ''

while True: 
    string_nova = string_nova + '*' + nome[indice]
    indice += 1
    if indice == len(nome):
        string_nova = string_nova + '*'
        break
        
print(string_nova)

# Aula 66
while True:
    try:
        resultado = 0
        valor1 = float(input('Favor inserir o valor 1: ' ))
        valor2 = float(input('Favor inserir o valor 2: ' ))
        conta = str(input('Favor inserir a operação matemática: ' ))
        if conta == '+':
            resultado = valor1 + valor2
            print(f'Resultado de {valor1} + {valor2} é {resultado}')
        elif conta == '-':
            resultado = valor1 - valor2
            print(f'Resultado de {valor1} - {valor2} é {resultado}')
        elif conta == '*':
            resultado = valor1 * valor2
            print(f'Resultado de {valor1} * {valor2} é {resultado}')
        elif conta == '/':
            resultado = valor1 / valor2
            print(f'Resultado de {valor1} / {valor2} é {resultado}')
        else:
            print('Você inseriu uma operação inexistente!')
    except:
        print('Algum dado foi inserido incorretamente!')
    sair = input('Você deseja [s]air?: ')..lower().startswith('s')
    if sair is True:
        break

# Aula 69
string = 'Valor qualquer'
i=0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
    #se houver um break, ele vai pular o else.
else:
    print('O Else foi executado!')
    
# Aula 70
frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum'

#print(frase.lower().count('python')) #upper()
indice = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while indice < len(frase):
    letra_atual = frase[indice]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    if letra_atual == ' ':
        indice += 1
        continue
    if apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_que_apareceu_mais_vezes = letra_atual
    #print(letra_atual, quantas_vezes_letra_apareceu)
    indice += 1
print(f'A letra que apareceu mais vezes foi "{letra_que_apareceu_mais_vezes}" que apareceu {apareceu_mais_vezes} vezes!')

# Aula 72
texto = 'Python'
for letra in texto:
    print(letra)
    
# Aula 73
#range(start,stop,step)
numeros = range(10)
for valor in numeros:
    print(valor)

numeros = range(5, 10)
for valor in numeros:
    print(valor)

numeros = range(5, 10, 2)
for valor in numeros:
    print(valor)
    
# Aula 74
texto = iter('Luiz') #.__iter__()
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

# for letra in texto:
texto = 'luiz'
iterador = iter(texto)

While True:
    try: 
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
        
# Aula 75
for i in range(10):
    if == 2:
        print('i é 2, pulando...')
        continue
    if i == 8:
        print('i é 8, não vai executar o ELSE!')
        break
    for j in range(1,3):
        print(i, j)
else:
    prin('For completo com sucesso!')
        
# Aula 76
palavra = 'amor'
letra = ''
revisada = ''
indice = 0
tentativas = 0

while True:
    letra = input('Insira a letra: ')
        
    if len(letra) > 1:
        print('Você digitou mais que uma letra na tentativa!')
        continue
    
    for letras in palavra:
        if palavra[indice] == letra:
            revisada += palavra[indice]
        else:
            revisada += '*'
        indice += 1
    print(revisada)
    indice = 0
    
    tentativas += 1

# Aula 78
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra por vez!')
        continue
        
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!!')
        print('A palavra era', palavra_secreta)
        print(f'Você precisou de {tentativas}!')
        break
        
# Aula 80
lista = [123, True, 'Wolnei', 1.2, []]
print(lista, type(lista))
lista[0] = 'Maria'
print(lista[0], type(lista[0]))

# Aula 81 - CREATE, READ, UPDATE, DELETE
lista = [1,2,3,4]
lista[2] = 300
del lista[1] 
print(lista)
lista.append(50)
lista.pop() #remove último elemento.

# Aula 82
lista = [1,2,3,4]
del lista[-1]
lista.clear()
lista.insert(0,5) #posição, valor

# Aula 83 - Concatenando e estendendo listas em Python.
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)

# Aula 84 - a lista aponta para o mesmo registro na memória!
lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_a[0] = ('Pedro')
print(lista_b)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()
lista_a[0] = ('Pedro')
print(lista_a)
print(lista_b)

# Aula 85
lista = ['Luiz', 'Maria']
for each in lista:
    print(each, type(each))

# Aula 86
lista = ['Luiz', 'Maria', 'Helena']
indice = 0

for each in lista:
    print(indice, ' - ', each)
    indice += 1
#------------------------------------    
lista = ['Luiz', 'Maria', 'Helena']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    
# Aula 87
nomes = ['Luiz', 'Maria', 'Helena']
nome1, nome2, nome3 = nomes
print(nome2)

nome1, *resto = ['Luiz', 'Maria', 'Helena']
print(nome1, resto)

_, nome2, *_ = ['Luiz', 'Maria', 'Helena']
print(nome2)

# Aula 88
nomes = 'Luiz', 'Maria', 'Helena'
print(nomes[-1])
print(nomes)

nomes = ['Luiz', 'Maria', 'Helena']
nomes = tuple(nomes)
nomes = list(nomes)
print(nomes)

# Aula 89
lista = ['Luiz', 'Maria', 'Helena']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)
    
#------------------------------------
lista = ['Luiz', 'Maria', 'Helena']
lista.append('João')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

#------------------------------------
lista = ['Luiz', 'Maria', 'Helena']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome)
    
# Aula 90
import os
lista = []

while True: 
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').upper()
    
    if opcao == 'I': #inserir na lista.
        produto = input('Digite o que deseja inserir a lista: ')
        lista.append(produto)
        os.system('clear')
    elif opcao == 'A': #apagar produto da lista
        try:
            for indice, item in enumerate(lista):
                print(indice, ' - ',item)
            delete = int(input('Digite o número do produto que deseja excluir: '))
            del lista[delete]
            os.system('clear')
        except ValueError:
            print('Código inserido incorretamente. Não foi possível excluir o produto!')
        except IndexError:
            print('Código inserido incorretamente. Não foi possível excluir o produto!')
    elif opcao == 'L': #listar produtos
        os.system('clear')
        if len(lista) == 0:
            print('lista vazia!')
        
        for indice, item in enumerate(lista):
            print(indice, ' - ',item)
    else:
        print('Você selecinou opção inválida/inexistente!')
        
# Aula 92
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(f'{numero_3:.2f}')
print(round(numero_3,3))

# Aula 93
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)

lista_frases = frase.split(',')
print(lista_frases)

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())
    
frases_unidas = ', '.join('abc')
print(frases_unidas)

# Aula 94
salas = ['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda', (1,2,3,4)]
print(salas[2][3][2])

for sala in salas:
    for item in sala:
        print(item)
    #print(sala)
    
# Aula 95
# Detalhes sobre o interpretador do Python.

# Aula 96
lista = ['Maria','Helena',1,2,3,'Eduarda']
a,b,*_, u = lista
print(a,u)
print(*lista)

# Aula 97 - Operação ternária com Python (if e else de uma linha)
condicao = 10 == 11 #False
variavel = 'valor' if condicao else 'outro valor'
print(variavel)

# Aula 98 - Validador CPF
import os

while True:
    entrada_cpf = input('Insira seu CPF: ')
    #entrada_cpf = input('Insira seu CPF: ').replace('-','').replace('/','').replace('.','').replace('/','')
    #entrada_cpf = re.sub(r'[^0-9],'', entrada_cpf)
    caracteres_invalidos = ['-', '.', '/', ',']
    multiplicador = 10
    somador_1 = 0
    somador_2 = 0
    
    try:
        os.system('clear')
        for i in caracteres_invalidos:
           entrada_cpf = entrada_cpf.replace(i, '')
        
        for numero in entrada_cpf:
            somador_1 = somador_1 + (int(numero) * multiplicador)
            multiplicador -= 1
            if multiplicador == 1:
                break
        digito_x = 11-(somador_1 % 11)
        multiplicador = 11
        
        if digito_x>9:
            digito_x = 0
        
        for numero in entrada_cpf:
            somador_2 = somador_2 + (int(numero) * multiplicador)
            multiplicador -= 1
            if multiplicador == 2:
                somador_2 = somador_2 + (2 * digito_x)
                break        
        digito_y = 11-(somador_2% 11)
        
        if digito_y>9:
            digito_y = 0
        
        numero_9 = int(entrada_cpf[9])
        numero_10 = int(entrada_cpf[10])
        
        if len(entrada_cpf) == 11 and digito_x == numero_9 and digito_y == numero_10:
            print(f'O CPF {entrada_cpf[0:3]}.{entrada_cpf[3:6]}.{entrada_cpf[6:9]}-{digito_x}{digito_y} é válido!')
        else:
            print(f'Os códigos validadores do CPF {entrada_cpf[0:3]}.{entrada_cpf[3:6]}.{entrada_cpf[6:9]}-{digito_x}{digito_y} são inválidos!')
        
    except:
        print(f'O CPF informado "{entrada_cpf}" está incorreto!')

# Inicio Seção 4 !!!

# Aula 105 
def Python():
    print('teste')
Python() 

def imprimir(a,b,c): #parametro(argumento)
    print(a,b,c)
imprimir(1,2,3)
imprimir('A','B','C')

def saudacao(nome):
    print(f'Olá, {nome}!')
saudacao('Wolnei')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

# Aula 106 - argumentos nomeados e argumentos posicionais
def soma(x,y):
    print(f'{x=} {y=}','|','x + y =', x+y)
soma(10,10)
soma(20,20)

def soma(x,y,z):
    print(f'{x=} {y=} {z=}','|','x + y + z =', x+y+z)
soma(x=1,z=3,y=2)

# Aula 107
def soma(x, y, z=0):
    if z:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0) # não considera z=0

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0) # considera z=0

# Aula 108
x=1
def escopo():
    x=10
    def outra_funcao():
        y=2
        print(x,y)
    outra_funcao()
    print(x)    
escopo()
print(x)

x=1
def escopo():
    global x
    x=10
    def outra_funcao():
        global x
        y=2
        print(x,y)
    outra_funcao()
    print(x)    
escopo()
print(x)

# Aula 109 - escopo global & local - Call Stack

# Aula 110
variavel = print('Teste')
print(variavel)
print(variavel is None)

def soma(x,y):
    return x + y
soma1 = soma(2,2)
soma2 = soma(3,3)
print(soma1+soma2)

# Aula 111-2
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
conta = soma(1,2,3,4,5,6)
print(conta)

numeros = 1,2,3,4,5,6
print(*numeros) #desempacota a tupla.

# Aula 113
def conta(*args):
    multiplicacao = 1
    for numero in args:
        multiplicacao = multiplicacao * numero
    return multiplicacao
    
def par_impar(*args):
    if conta_1%2==0:
        print(f'O Resultado da conta é {conta_1} é ele é PAR !')
    else:
        print(f'O Resultado da conta é {conta_1} é ele é IMPAR !')
    
conta_1 = conta(1,9)
par_impar(conta_1)

#programa com mais entradas:
import os

lista = []
while True:
    entrada = int(input('Insira um valor na conta: '))
    lista.append(entrada)
    pergunta = input('Deseja inserir novos números? [s]sim [n]não: ').lower()
    os.system('clear')
    if pergunta == 'n':
        break
    
def conta(lista):
    multiplicacao = 1
    for numero in lista:
        multiplicacao = multiplicacao * numero
        #print(multiplicacao)
    return multiplicacao
    
def par_impar(*args):
    if conta_1%2==0:
        print(f'O Resultado da conta é {conta_1} é ele é PAR !')
    else:
        print(f'O Resultado da conta é {conta_1} é ele é IMPAR !')
    
conta_1 = conta(lista)
par_impar(conta_1)

# Aula 114
def saudacao(msg):
    return msg
print(saudacao('Bom dia!'))

# Aula 115
'''
Higher Order Functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
'''

# Aula 116
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar
    
s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')
print(s1('Wolnei'))
print(s2('Wolnei'))

# Aula 117
numero = int(input('Insira o número a ser calculado: '))

def duplicar(numero):
    return numero*2
    
def triplicar(numero):
    return numero*3
    
def quadriplicar(numero):
    return numero*4

conta = duplicar(numero)
print(f'O Valor duplicado é {conta}!')

conta = triplicar(numero)
print(f'O Valor triplicado é {conta}!')

conta = quadriplicar(numero)
print(f'O Valor quadriplicado é {conta}!')

#solução Udemy
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))

# Aula 119 - dicionário
pessoa_1 = {
    'nome': 'Wolnei',
    'sobrenome': 'Hellmann Dircksen',
    'idade': 32,
    'altura': 1.75,
    'endereços': [
        {'rua': 'Frederico Jensen', 'numero': 4992},
        {'rua': 'Kurt Hering', 'numero': 30}
    ]
}
print(pessoa_1['nome'])
print(pessoa_1['idade'])
 
pessoa_2 = dict(nome='Luiz Otávio', sobrenome='Miranda')
print(pessoa_2)

# Aula 120 - dicionário - manipulando chaves e valores em dicionários
pessoa = {}
chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'
print(pessoa)

pessoa[chave] = 'Maria'
del pessoa['sobrenome']
print(pessoa)

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
#----------------------------------
pessoa = {}
pessoa['nome'] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'
pessoa['idade'] = 18
print(pessoa)

if pessoa.get('idade') >= 18:
    print('Maior de idade!')
else:
    print('Menor de idade!')
    
# Aula 121 # códigos para dicionários
pessoa = {
    'nome': 'Wolnei',
    'sobrenome': 'Hellmann Dircksen',
    'idade': 32,
    'altura': 1.75,
    'endereços': [
        {'rua': 'Frederico Jensen', 'numero': 4992},
        {'rua': 'Kurt Hering', 'numero': 30}
    ]
}
print(len(pessoa))
print(len(pessoa['endereços']))
print(pessoa.keys())
print(list(pessoa.keys()))
print(pessoa.values())
pessoa.setdefault('ano_nascimento', None)

for chaves in pessoa:
    print(chaves)
    
for chaves in pessoa.values():
    print(chaves)
    
for chave, valor in pessoa.items():
    print(chave, valor)
    
# Aula 122
d1 = {
    'c1': 1,
    'c2': 2,
}
d2 = d1 #direciona para mesmo registro de memória
d2['c1'] = 1000
print(d1['c1'])
#-----------------
d1 = {
    'c1': 1,
    'c2': 2,
}
d2 = d1.copy() #gera novo registro na memória
d2['c1'] = 1000
print(d1)
print(d2)
#-----------------
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}
d2 = d1.copy() #gera novo registro na memória, porém somente primeiro nivel de registros!
d2['c1'] = 1000
d2['l1'][1] = 99999
print(d1)
print(d2)
#-----------------
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}
d2 = copy.deepcopy(d1) #deu erro, verificar.
d2['c1'] = 1000
d2['l1'][1] = 99999
print(d1)
print(d2)

# Aula 123
pessoa = {
    'nome': 'Wolnei',
    'sobrenome': 'Hellmann Dircksen',
    'idade': 32,
    'altura': 1.75,
    'endereços': [
        {'rua': 'Frederico Jensen', 'numero': 4992},
        {'rua': 'Kurt Hering', 'numero': 30}
    ]
}
pessoa.get('nome')
pessoa.setdefault('ano_nascimento', None)
pessoa.pop('nome')
pessoa.popitem() #apaga ultimo registro

pessoa.update({
    'nome': 'Pedro',
    'idade': 28
})
pessoa.update(nome='Pedro', idade=28)

print(pessoa)

# Aula 125
import os
questao = 0
soma = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print(f'Pergunta: {perguntas[0]["Pergunta"]}')
for indice in perguntas[0]["Opções"]:
    print(questao, ')', indice)
    questao += 1
resposta = int(input('Insira o valor da resposta: '))
if resposta == 2:
    print('Acertou!')
    soma+=1
else:
    print('Resposta errada!')
    
os.system('clear')
questao = 0

print(f'Pergunta: {perguntas[1]["Pergunta"]}')
for indice in perguntas[1]["Opções"]:
    print(questao, ')', indice)
    questao += 1
resposta = int(input('Insira o valor da resposta: '))
if resposta == 0:
    print('Acertou!')
    soma+=1
else:
    print('Resposta errada!')
    
os.system('clear')
questao = 0

print(f'Pergunta: {perguntas[2]["Pergunta"]}')
for indice in perguntas[2]["Opções"]:
    print(questao, ')', indice)
    questao += 1
resposta = int(input('Insira o valor da resposta: '))
if resposta == 1:
    print('Acertou!')
    soma+=1
else:
    print('Resposta errada!')
    
os.system('clear')

if soma == 0:
    print('Você errou todas :-(')
else:
    print('Você acertou', soma)
#---------------------------------
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print('Pergunta', pergunta['Pergunta'])
    print()
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)

# Aula 126
s1 = set()
print(s1)

s1 = set()
s1 = {'Luiz',1 , 2, 3}
print(s1)

# Aula 127
s1 = {1,2,3,3,3,3,1}
print(s1)

l1 = [1,2,3,3,3,3,1]
s1 = set(l1)
l2 = list(s1)
print(l2)

# Aula 128
s1 = set()
s1.add('Luiz')
s1.update('wolnei')
print(s1)
s1.add(2)
print(s1)
s1.discard(2)
print(s1)
s1.clear()
print(s1)

# Aula 129
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 # união
print(s3)
s3 = s1 & s2 # intersessão
print(s3)
s3 = s1 - s2 # diferença (apenas os itens na esquerda S1)
print(s3)
s3 = s2 - s1 # diferença (apenas os itens na esquerda S2)
print(s3)
s3 = s1 ^ s2 # diferença simétrica
print(s3)

# Aula 133
lista = [4,2,6,8,7,9,2,1]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
def ordena(item):
    return item['nome']
lista.sort(key=ordena)
for item in lista:
    print(item)
    
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)
    
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
def exibir(lista):
    for item in lista:
        print(item)
    print()
l1 = sorted(lista, key=lambda item: item['nome'])
exibir(l1)

# Aula 135
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}
(a1,a2), (b1,b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)
#-----------------------------------    
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)

mostro_argumentos_nomeados(nome='Joana', sobrenome='Almeida')
mostro_argumentos_nomeados(**pessoa_completa)

# Aula 135
lista = [1 for numero in range(10)]
print(lista)

# Aula 137
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')

# Aula 139
lista = []
  for x in range(3):
    for y in range (3):
        lista.append((x,y))
print(lista)

# Aula 141
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'Categoria': 'Escritório'
}
dicionario={
    chave: valor
    for chave, valor
    in produto.items()
}
print(dicionario)

# Aula 142
lista = ['a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Luiz'}]
for dados in lista:
    print(dados, isinstance(dados, list))
    if isinstance(dados, list) is True:
        print(dados)   
    if isinstance(dados, (int, float)):
        print(dados, dados*2)
        
# Aula 143
# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy'if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))

# Aula 198 --> PascalCase para nome de classes
string = 'Luiz'
print(string.upper())
print(isinstance(string, str))

class Pessoa:
    ...
p1 = Pessoa()
print(p1)

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome #atributos
        self.idade = idade
p1 = Pessoa("Wolnei", 32)
p2 = Pessoa("Luiz", 18)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

# Aula 199 
class Pessoa:
    def __init__(self, nome, sobrenome): #método
        self.nome = nome #atributos
        self.sobrenome = sobrenome
p1 = Pessoa("Wolnei", "Hellmann")
print(p1.nome, p1.sobrenome)

# Aula 200
class Carro: # atributo e parametro
    def __init__(self, modelo):
        self.modelo = modelo
    def acelerar(self):
        print(f'{self.modelo} está acelerando!')
fusca = Carro("Fusca")
print(fusca.modelo)
print(fusca.acelerar())
    
# Aula 201
class Carro: # atributo e parametro
    def __init__(self, modelo):
        self.modelo = modelo
    def acelerar(self):
        print(f'{self.modelo} está acelerando!')
        
fusca = Carro("Fusca")
fusca.acelerar()
Carro.acelerar(fusca)

# Aula 202
class Animal:
    nome: 'Leão'
print(Animal.nome)

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('carne'))

# Aula 203
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando!')
            return
        print(f'{self.nome} está filmando!')
        self.filmando = True
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar!')
            return
c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()

# Aula 204
class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        #return self.ano_atual - self.idade
p1 = Pessoa("Wolnei", 32)
print(p1.get_ano_nascimento())

# Aula 205
class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        #return self.ano_atual - self.idade
p1 = Pessoa("Wolnei", 32)
print(p1.__dict__)

dados = {'nome': 'Pedro', 'idade': 18}
p2 = Pessoa(**dados)
print(p2.__dict__)

# Aula 144
# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)

# Aula 145
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__()
#iterator = iter(iterable)
print(next(iterator))

# Aula 146
import sys
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable)

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# Aula 147
try:
    def generator(n=0):
        yield 1
        print("Continuando...")
        yield 2
    gen = generator(n=0)
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("finalizado")
    
# Prática de POO (Python):
class Carro:
    def __init__(self, fabricante):
        self.fabricante = fabricante
class Marcas(Carro):
    def __init__(self, fabricante, modelo):
        super().__init__(fabricante)
        self.modelo = modelo
class Ano(Marcas):
    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo)
        self.ano = ano

Carro1 = Ano("FIAT", "Palio", 2014)
Carro2 = Ano("FIAT", "Pulse", 2021)
print(Carro1.fabricante, Carro1.modelo, Carro1.ano)
print(Carro2.fabricante, Carro2.modelo, Carro2.ano)

# Aula 209
class Pessoa:
    ano = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def metodo_de_classe(cls)
        print("Teste")
    @classmethod
    def criar_com_50_anos(cls, nome)
        return cls(nome, 50)
    
p1 = ("João")
p1.metodo_de_classe()
Pessoa.metodo_de_classe(p1)        

# Aula 210
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe():
        print("teste")        
c1 = Classe()
c1.funcao_que_esta_na_classe()

# Aula 211
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    def set_user(self, user):
        self.user = user
    def set_password(self, password):
        self.password = password   
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
c1 = Connection()
c1.set_user("wolnei")
c1.set_password("123")
print(c1.user, c1.password)
c2 = Connection.create_with_auth(c1.user, c1.password)

# Aula 212
class Caneta:
    def __init__(self, cor):
        self.cor = cor
    def get_cor(self):
        return self.cor
caneta = Caneta('Azul')
print(caneta.get_cor())

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    def get_cor(self):
        return self.cor_tinta
caneta = Caneta('Azul')
print(caneta.get_cor())

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    @property
    def cor(self):
        return self.cor_tinta
    @property
    def cor_tampa(self):
        return 123456
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)

# Aula 213
# getter ==> obter valor // Método não salva valor, apenas executa.
class Caneta:
    def __init__(self, cor):
        self._cor = self.cor
    @property
    def cor(self):
        return self.cor
    @cor.setter
    def cor(self, valor):
        self._cor=valor
        
caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)

'''
- Classes allow you to create user-defined data structures. Classes define functions called methods.
- Instance methods are functions that you define inside a class and can only call on an instance of that class.
'''
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
dog1 = Dog("Rufus", 8)
print(Dog.description(dog1))
print(Dog.speak(dog1, 'au-au'))

print(dog1.description())
print(dog1.speak('au-au'))
#=============================================
class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value
        
texto1 = Label("Fruits", "JetBrains Mono NL")
print(texto1.get_text())
texto1.set_text("Banana")
print(texto1.get_text())
#=============================================
class Label:
    def __init__(self, text, font):
        self.set_text(text)
        self.font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value.upper()  # Attached behavior
        
texto = Label("Fruits", "JetBrains Mono NL") # Fruits
texto.set_text(texto.get_text())
print(texto.get_text()) # FRUITS

# Aula 214 - modificadores de acesso: public, protected, private.
''' OBSERVAÇÕES:
- sem underline: public
- _ (um underline): protected
- __ (dois underlines): private
'''
class Foo:
    def __init(self):
        self.public = 'isso é público'
        self._protected = 'isso é progido'
        self.__private = 'isso é private'
    def metodo_público(self):
        self._metodo_protected()
        print(self.__private)
        return 'metodo_público'
    def _metodo_protected(self):
        return '_metodo_protected'
    def __metodo_private(self):
        return 'metodo private'

# Aula 215
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())

# Aula 216
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())

# Aula 217
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    def mostrar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua,endereco.numero)
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
        
cliente1 = Cliente("Maria")
cliente1.inserir_enderecos("Av. Brasil", 54)
cliente1.inserir_enderecos("Rua Jervis", 6745)
cliente1.mostrar_enderecos()

# Aula 218 
# Exercício com classes
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)

# Aula 219/220
# Classe principal: super class, base class, parent class
# Classes filhas: sub class, child class, devired class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)
class Cliente(Pessoa):
    ...
class Aluno(Pessoa):
    ...
p1 = Pessoa("Wolnei", "Dircksen")
a1 = Aluno("Filipe", "Regis")
p1.falar_nome_classe()
a1.falar_nome_classe()

# Aula 221/222
class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()

# Aula 150
try:
    a = 18
    b = 0
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')

# Aula 151
try:
    print(111)
except ZeroDivisionError:
    print('DIVISÃO POR ZERO!')
finally:
    print(222)
    
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Jogar error numa box:")
        raise
print(divide(8,0))
#===========================================
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True
def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True
def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d
print(divide(8, '0'))

# Aula 153
from sys import exit, platform
from sys import platform as pt

# aula 154
import (nome_do_módulo)

# Aula 156
import importlib
import aula98_m

print(aula98_m.variavel)
for i in range(10):
    importlib.reload(aula98_m)
    print(i)
print('Fim')

# Aula 157
from aula_package.modulo import soma
import package.modulo
from package import modulo

__all__ = [
     'variavel',
     'soma_do_modulo',
     'nova_variavel',
]
variavel = 'Alguma coisa'
def soma_do_modulo(x, y):
    return x + y
nova_variavel = 'OK'

# Aula 161
# dados/produtos_modulo.py
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# dados/__init__.py
from dados.produtos_modulo import produtos
# aula100.py
import copy
from dados import produtos
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')

# Aula 163
def soma(x, y):
    return x + y
def multiplica(x, y):
    return x * y
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))

