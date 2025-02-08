import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER, password=PASSWORD, host=HOST, port=PORT, dbname=DBNAME
    )
    print("Connection successful!")

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    query = """
        SELECT 
            c.id, 
            c.name, 
            c.email, 
            p.amount
        FROM clients c 
        INNER JOIN payments p ON c.id = p.client_id;
    """

    # Example query
    cursor.execute(query)
    result = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")


# Print the result
print("Result as a list of tuples:")
for row in result:
    print(row)

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
print("\nResult as a DataFrame:")
print(df)
