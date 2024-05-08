import sqlite3

con = sqlite3.connect("database.db")
c = con.cursor()

def create_categories_table(month_choosen,year):
    table_name = f"{month_choosen.lower()}_{year}"
    c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    cat_ID TEXT,
                    expenses REAL,
                    date BLOB,
                    note BLOB
                  )""")
    # for category, color in zip(categories, colors): #python will ignore the exceeding numbers of values and match to the lower one instead
    #     c.execute(f"INSERT INTO {table_name} (cat_ID, expenses, date, note) VALUES (?, ?, ?)", ("", "", "", ""))
        
def add_new_categories(new_category):
    table_name = "cat_ID_with_colour"
    c.execute("SELECT cat_ID FROM cat_ID_with_colour")
    row = c.fetchall()
    new_row = len(row) + 1
    c.execute(f"INSERT INTO {table_name} (cat_ID, category, colour) VALUES (?, ?, ?)", (new_row, new_category,0))
    con.commit()
    
def add_new_colour(colour_for_category,category_for_colour):
    table_name = "cat_ID_with_colour"
    c.execute(f"UPDATE {table_name} SET colour = ? WHERE category= ? ", (colour_for_category,category_for_colour))  
    con.commit()
    
def update_categories_list():
    global categories
    table_name = "cat_ID_with_colour"
    c.execute(f"SELECT category FROM {table_name}")
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

# create_categories_table()
con.commit()

#create relation-database
#create a table just for categories use cat-id (1 - food; 2- Pet)
#then just refer to cat-id in the month table 