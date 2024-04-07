import os
from dotenv import load_dotenv

print(os.environ)
load_dotenv()
chave = os.getenv('TOKEN01')
print(chave)