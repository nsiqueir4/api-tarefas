import os
from os import getenv

import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conexao = psycopg2.connect(
        dbname=os.getenv(''),
        user=os.getenv(''),
        password=os.getenv(''),
        host=getenv(''),
        port=getenv('')
    )
    return conexao