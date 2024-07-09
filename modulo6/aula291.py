from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_projeto = Path(__file__)
print(caminho_projeto)

print(caminho_projeto.parent)
print(caminho_projeto.parent.parent)

print(Path.home())

caminho_projeto = Path()
arquivo = caminho_projeto / 'arquivo_teste.txt'
arquivo.touch() #cria arquivo
print(arquivo)
arquivo.unlink() #exclui arquivo

#caminho_pasta.mkdir(exist_ok=True)