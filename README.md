# Description

This project allows you to compare two ways of working with a database:

1. Using raw SQL queries.
2. Using an ORM, in this case, SQLAlchemy.

# Installation

To use this project, follow these steps:

1. Install Docker Desktop.
2. Install VS Code.
3. Install the Dev Containers extension for VS Code.
4. Clone the repository and open it in a Dev Container. To do this:
   1. Open VS Code.
   2. Go to **View/Command Palette...**
   3. Run **Dev Containers: Clone repository in a named container volume**.

# Execution

1. You need to configure an `.env` file with the database connection variables.
2. In the `src/sql` folder, you will find a sample database that you can use.
3. The ORM models are defined in the `src/models` folder.
4. The files `main_sqlalchemy.py` and `main_sql.py` are the ones you should use to run the project.
