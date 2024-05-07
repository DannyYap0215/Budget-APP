import sqlite3

con = sqlite3.connect("database.db")
c = con.cursor()

def create_categories_table(month, year):
    table_name = f"{month.lower()}_{year}"
    c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    category_name TEXT,
                    color TEXT,
                    budget REAL
                  )""")
    for category, color in zip(categories, colors): #python will ignore the exceeding numbers of values and match to the lower one instead
        c.execute(f"INSERT INTO {table_name} (category_name, color, budget) VALUES (?, ?, ?)", (category, color, 0))
        
def add_new_categories(month_choosen,new_category):
    table_name = f"{month_choosen.lower()}_{year}"
    c.execute(f"INSERT INTO {table_name} (category_name, color, budget) VALUES (?, ?, ?)", (new_category, "",0))
    con.commit()
    
def add_new_colour(month_choosen,colour_for_category,category_for_colour):
    table_name = f"{month_choosen.lower()}_{year}"
    c.execute(f"UPDATE {table_name} SET color = ? WHERE category_name= ? ", (colour_for_category,category_for_colour))  
    con.commit()
    
def update_categories_list(month_choosen):
    global categories
    table_name = f"{month_choosen.lower()}_{year}"
    c.execute(f"SELECT category_name FROM {table_name}")
    list_through_categories = c.fetchall()
    categories = []
    for i in range(len(list_through_categories)) :
        categories.append(list_through_categories[i][0])
    return categories
        

    
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = 2024

colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "cyan",
    "magenta",
    "black",
    "white",
    "gray",
    "lightgray",
    "darkgray",
    "lightblue",
    "darkblue",
    "lightgreen",
    "darkgreen",
    "lightred",
    "darkred",
    "lightyellow",
    "darkyellow",
    "lightorange",
    "darkorange",
    "lightpurple",
    "darkpurple"
]
# categories = [
#     "Food",
#     "Transport",
#     "Household",
#     "Pets",
#     "Apparel",
#     "Beauty",
#     "Health",
#     "Education",
#     "Social Life",
#     "Gift",
# ]

#don't run this ; the tables had already been created
# for month in months:
#     create_categories_table(month, year)

update_categories_list("January")
con.commit()

