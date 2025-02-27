import os

import pandas as pd
from dotenv import load_dotenv

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from src.models.mechanical_shop.client import Client
from src.models.mechanical_shop.product import Product
from src.models.mechanical_shop.sales import Sales

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

try:
    query = (
        select(Client.dni, Client.name, Product.description, Sales.sold_date)
        .select_from(Client)
        .join(Sales, Client.client_id == Sales.client_id)
        .join(Product, Product.product_id == Sales.product_id)
    )

    results = session.execute(query).fetchall()
finally:
    session.close()

# Print the result
for row in results:
    print(row)

# Convert the result to a DataFrame
df = pd.DataFrame(results)
print("\nResult as a DataFrame:")
print(df)

# Print using attribute names
print("\nResult using attribute names:")
for row in results:
    print(row.dni, row.name, row.description, row.sold_date)
