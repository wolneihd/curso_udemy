import os
from dotenv import load_dotenv

#senha = os.getenv('SENHA')
#print(senha)

load_dotenv()

print(os.getenv('BD_USER'))