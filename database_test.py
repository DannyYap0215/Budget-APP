import sqlite3

def create_categories_table(month, year):
    table_name = f"categories_{month.lower()}_{year}"
    c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    category_id INTEGER PRIMARY KEY,
                    category_name TEXT NOT NULL,
                    color TEXT,
                    budget REAL
                  )""")
    print(f"Table for {month} {year} categories created successfully.")

# Establish the database connection
con = sqlite3.connect("database.db")
c = con.cursor()

# Create a table for January 2024 categories
create_categories_table("January", 2024)

# Insert sample data into the January 2024 categories table
c.execute("INSERT INTO categories_january_2024 (category_name, color, budget) VALUES (?, ?, ?)", ("Rent", "red", 1000))
c.execute("INSERT INTO categories_january_2024 (category_name, color, budget) VALUES (?, ?, ?)", ("Food", "green", 500))

# Query the Users table
c.execute("SELECT * FROM Users WHERE Age = ?", (19,))
print(c.fetchall())

# Commit changes and close connection
con.commit()
con.close()
