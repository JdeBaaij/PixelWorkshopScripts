import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('DOMAIN')
KEY = os.getenv('MASTER_KEY')
HEADERS = {'Content-Type': 'application/json'}