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

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    query = """
        SELECT 
            c.dni, 
            c.name, 
            p.description, 
            s.sold_date
        FROM client c
        INNER JOIN sales s ON c.client_id = s.client_id
        INNER JOIN product p ON p.product_id = s.product_id
    """

    # Example query
    cursor.execute(query)
    result = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

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
