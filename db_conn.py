import asyncpg
from creds import host, port, dbname, user, password

# Function to connect to the database
async def connect_to_database():
    conn = await asyncpg.connect(
       database=dbname, user=user, password=password, host=host, port=port
    )
    return conn