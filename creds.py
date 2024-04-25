import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connection parameters from environment variables
host = os.getenv('host')
port = os.getenv('port')
dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')