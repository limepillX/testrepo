import os

from dotenv import load_dotenv

load_dotenv()

print(os.getenv('TEST'))
print(os.getenv('TEST1'))
print(os.getenv('TEST3'))

