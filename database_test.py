import sqlite3

con = sqlite3.connect("database.db")
c = con.cursor()

#creating tables
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
        
def create_budget_for_monthly_usage(month) :
    table_name = f"budget_for_{month.lower()}_{year}"
    c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    cat_ID TEXT,
                    budget_allocated REAL,
                    budget_used REAL
                  )""")
    
def create_table_containing_allocated_income_for_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    table_name = "allocated_income_for_month_2024"
    c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    months TEXT,
                    allocated_income REAL
                  )""")
    con.commit()
    for month in months:
        c.execute(f"INSERT INTO {table_name} (months, allocated_income) VALUES (?, ?)", (month,0))
        con.commit()
        
def create_expensesID_table(): 
    table_name = "expenses_ID_with_month"
    c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    expenses_ID TEXT,
                    months TEXT
                  )""")
    con.commit()
    
#main functions
def add_new_categories(new_category): #used in set_categories.py
    table_name = "category_data"
    c.execute("SELECT cat_ID FROM category_data")
    row = c.fetchall()
    new_row = len(row) + 1
    c.execute(f"INSERT INTO {table_name} (cat_ID, category, colour) VALUES (?, ?, ?)", (new_row, new_category,0))
    con.commit()
    
def add_new_colour(colour_for_category,category_for_colour): #used in set_categories.py
    table_name = "category_data"
    c.execute(f"UPDATE {table_name} SET colour = ? WHERE category= ? ", (colour_for_category,category_for_colour))  
    con.commit()
    
def update_categories_list(): #used in set_categories.py
    global categories
    table_name = "category_data"
    c.execute(f"SELECT category FROM {table_name}")
    list_through_categories = c.fetchall()
    categories = []
    for i in range(len(list_through_categories)) :
        categories.append(list_through_categories[i][0])
    return categories

def delete_categories(category_to_delete): #used in set_categories.py
    c.execute(f"SELECT cat_ID FROM category_data WHERE category = ? ",(category_to_delete,))
    cat_ID = c.fetchone()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = c.fetchall()
    for table in tables:
        if table[0] == "allocated_income_for_month_2024" or table[0] == "expenses_ID_with_month": #2 hrs wasted here - Danny
            pass
        else:
            print(table)
            table_name = f"{table[0]}"
            c.execute(f"DELETE FROM {table_name} WHERE cat_ID = ? ", (cat_ID[0],))
            con.commit()    
        
        
    
def allocating_budget_to_table(month_choosen, allocated_budget, category_selected):
    # Retrieve the cat_ID corresponding to the selected category from the category_data table
    c.execute("SELECT cat_ID FROM category_data WHERE category = ?", (category_selected,))
    ID_row = c.fetchone()  # Fetch only one row
    con.commit()
    
    if ID_row:
        cat_ID = ID_row[0]
        table_name = f"budget_2024"
        c.execute(f"SELECT cat_ID FROM {table_name} WHERE cat_ID = ?", (cat_ID,))
        existing_row = c.fetchone()
        con.commit()
        if existing_row:
            c.execute(f"UPDATE {table_name} SET budget_allocated = ? WHERE cat_ID = ?", (allocated_budget, cat_ID))
            con.commit()
        else:
            c.execute(f"INSERT INTO {table_name} (cat_ID, months, budget_allocated, budget_used) VALUES (?, ?, ?, ?)", (cat_ID, month_choosen, allocated_budget, 0))
            con.commit()
    

def allocated_income_for_month(income_allocated,selected_month_menu): #used in set_income.py
    table_name = "allocated_income_for_month_2024"
    c.execute(f"UPDATE {table_name} SET allocated_income = ? WHERE months= ? ", (income_allocated,selected_month_menu))  
    con.commit()


def insert_expenses_to_table(expenses_date,expenses_amount,expenses_categories,expenses_note):
    numbers_to_month = {
        "01":"January", 
        "02":"February", 
        "03":"March", 
        "04":"April", 
        "05":"May", 
        "06":"June", 
        "07":"July", 
        "08":"August", 
        "09":"September", 
        "10":"October", 
        "11":"November", 
        "12":"December"
    }
    
    month = str(expenses_date).split("-")[1]
    month = numbers_to_month[month]
    
    c.execute("SELECT expenses_ID FROM daily_expenses")
    row = c.fetchall()
    if len(row) == 0:
        expenses_ID = 1000
    else:
        expenses_ID = len(row) + 1000
        
    # c.execute(f"INSERT INTO expenses_ID_with_month (expenses_ID, months) VALUES (?, ?)", (expenses_ID, month))
    # con.commit()
    
    c.execute("SELECT cat_ID FROM category_data WHERE category = ?", (expenses_categories,))
    cat_ID = c.fetchone()  # Fetch ID
    table_name = f"daily_expenses"
    c.execute(f"INSERT INTO {table_name} (expenses_ID, months, cat_ID, expenses, date, note) VALUES (?, ?, ?, ?, ?, ?)", (expenses_ID, month, cat_ID[0], expenses_amount,expenses_date,expenses_note))
    con.commit()
    c.execute("SELECT budget_used FROM budget_2024 WHERE cat_ID = ?  AND months = ?",(cat_ID[0][0],month))
    budget_value = c.fetchone()
    if budget_value is None:
        budget_value = 0
    else:
        budget_value = budget_value[0]
    budget_value = budget_value + float(expenses_amount) 
    cat_ID = c.execute("SELECT cat_ID FROM category_data WHERE category = ?",(expenses_categories,))
    cat_ID = c.fetchall()
    c.execute("UPDATE budget_2024 SET budget_used = ? WHERE cat_ID = ?  AND months = ? ",(budget_value,cat_ID[0][0],month))
    con.commit()
    
    
# def search_history():
#     c.execute("SELECT")
    

    
# def get_income_piechart() :
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#     for month in months:
#     global rows
#     c.execute(f"SELECT months , allocated_income FROM allocated_income_for_month_2024")
#     months_and_allocated_income = c.fetchall()
#     rows = months_and_allocated_income
    
    


#random values
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
#     create_budget_for_monthly_usage(month)

# create_categories_table()

#create relation-database
#create a table just for categories use cat-id (1 - food; 2- Pet)
#then just refer to cat-id in the month table 

