import sqlite3

def create_categories_table(month, year):
    table_name = f"{month.lower()}_{year}"
    c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    category_name TEXT,
                    color TEXT,
                    budget REAL
                  )""")
    for category in categories:
        c.execute(f"INSERT INTO {table_name} (category_name, color, budget) VALUES (?, ?, ?)", (category, '', 0))
    

con = sqlite3.connect("database.db")
c = con.cursor()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = 2024

categories = [
    "Food",
    "Transport",
    "Household",
    "Pets",
    "Apparel",
    "Beauty",
    "Health",
    "Education",
    "Social Life",
    "Gift",
]


for month in months:
    create_categories_table(month, year)

con.commit()
con.close()
