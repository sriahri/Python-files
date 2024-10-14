
import sqlite3

def connect_db():
    try:
        return sqlite3.connect('icecream')
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table_allergens():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS allergens (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
        ''')
        conn.commit()
        conn.close()
    else:
        print("Failed to create table: unable to connect to the database.")

def create_ingredients_table():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE ingredients (
        id       INTEGER        PRIMARY KEY,
        name     TEXT (50, 2)   NOT NULL,
        quantity INTEGER (3, 2) NOT NULL
        )

        ''')
        conn.commit()
        conn.close()
    else:
        print("Failed to create ingredients table: unable to connect to the database.")

def create_suggestions_table():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE suggestions (
            id                INTEGER      PRIMARY KEY,
            customer_name     TEXT (15, 2) NOT NULL,
            flavor_suggestion TEXT (50, 2) NOT NULL,
            allergy_concerns  TEXT (50, 2) 
            )
        ''')
        conn.commit()
        conn.close()
    else:
        print("Failed to create ingredients table: unable to connect to the database.")

def create_seasonal_flavor_table():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE seasonal_flavors (
            id          INTEGER       PRIMARY KEY,
            name        TEXT (20, 2)  NOT NULL,
            description TEXT (100, 2),
            ingredients TEXT (100, 2) 
            )

        ''')
        conn.commit()
        conn.close()
    else:
        print("Failed to create ingredients table: unable to connect to the database.")


def create_table():
    create_table_allergens()
    create_ingredients_table()
    create_suggestions_table()
    create_seasonal_flavor_table()


def add_ingredient(name, quantity):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO ingredients (name, quantity)
        VALUES (?, ?)
        ''', (name, quantity))
        conn.commit()
        conn.close()
    else:
        print("Failed to add ingredient: unable to connect to the database.")

def add_suggestion(customer_name, flavor_suggestion, allergy_concerns):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO suggestions (customer_name, flavor_suggestion, allergy_concerns)
        VALUES (?, ?, ?)
        ''', (customer_name, flavor_suggestion, allergy_concerns))
        conn.commit()
        conn.close()
    else:
        print("Failed to add suggestion: unable to connect to the database.")

def add_allergen(allergen):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO allergens (name, description) VALUES (?, ?)
        ''', (allergen['name'], allergen['description']))
        conn.commit()
        conn.close()
    else:
        print("Failed to add allergen: unable to connect to the database.")

def list_seasonal_flavors():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seasonal_flavors')
        flavors = cursor.fetchall()
        conn.close()
        return flavors
    else:
        print("Failed to list seasonal flavors: unable to connect to the database.")
        return []



def search_flavors(keyword):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        sql_query = '''
        SELECT * FROM seasonal_flavors
        WHERE name LIKE ? OR description LIKE ?
        '''
        print(f"Executing SQL query: {sql_query} with keyword: {keyword}")
        cursor.execute(sql_query, (f'%{keyword}%', f'%{keyword}%'))
        results = cursor.fetchall()
        print(f"Search results: {results}")
        conn.close()
        return results
    else:
        print("Failed to search flavors: unable to connect to the database.")
        return []

def main():
    create_table()  # Ensure all tables are created at the start
    cart = []
    while True:
        print("\nIce Cream Parlor Cafe")
        print("1. List Seasonal Flavors")
        print("2. Search Flavors")
        #print("3. Add Seasonal Flavor")
        print("3. Add Ingredient")
        print("4. Add Customer Suggestion")
        print("5. Add Allergen")
        print("6. Add Flavor to Cart")
        print("7. View Cart")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            flavors = list_seasonal_flavors()
            for flavor in flavors:
                print(f"ID: {flavor[0]}, Name: {flavor[1]}, Description: {flavor[2]}, Ingredients: {flavor[3]}")
        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            results = search_flavors(keyword)
            for result in results:
                print(f"ID: {result[0]}, Name: {result[1]}, Description: {result[2]}, Ingredients: {result[3]}")
        # elif choice == '3':
        #     name = input("Enter flavor name: ")
        #     description = input("Enter flavor description: ")
        #     ingredients = input("Enter flavor ingredients: ")
        #     add_seasonal_flavor(name, description, ingredients)
        elif choice == '3':
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter ingredient quantity: "))
            add_ingredient(name, quantity)
        elif choice == '4':
            customer_name = input("Enter your name: ")
            flavor_suggestion = input("Enter flavor suggestion: ")
            allergy_concerns = input("Enter any allergy concerns: ")
            add_suggestion(customer_name, flavor_suggestion, allergy_concerns)
        elif choice == '5':
            name = input("Enter allergen name: ")
            description = input("Enter allergen description: ")
            add_allergen(name, description)
        elif choice == '6':
            flavor_id = input("Enter flavor ID to add to cart: ")
            cart.append(flavor_id)
            print(f"Flavor ID {flavor_id} added to cart. Current cart: {cart}")
        elif choice == '7':
            print("Your Cart:", cart)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()