#PROGRAM TO VERIFY WHETHER THE .env FILE IS CREATED CORRECT IN PYCHARM AND CORRECTLY PRINTING THE RIGHT BASE_URL VALUE

from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv('BASE_URL'))