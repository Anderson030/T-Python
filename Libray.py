# Library Catalog Manager
# Author: ChatGPT (based on user requirements)
# Description: A simple command-line system for managing a book catalog

from datetime import datetime

# Initial catalog with 5 example books
catalog = [
    {"title": "Cien Años de Soledad", "author": "Gabriel García Márquez", "genre": "Novel", "year": 1967, "quantity": 3, "price": 25000},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "year": 1949, "quantity": 5, "price": 18000},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "year": 1960, "quantity": 4, "price": 20000},
    {"title": "Don Quixote", "author": "Miguel de Cervantes", "genre": "Classic", "year": 1605, "quantity": 2, "price": 30000},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "year": 1925, "quantity": 6, "price": 22000},
]

# Function to register a new book
def register_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    
    try:
        year = int(input("Enter publication year: "))
        if year > datetime.now().year or year < 1800:
            print("Invalid year. Enter a value between 1800 and 2024.")
            return
        quantity = int(input("Enter available quantity: "))
        price = float(input("Enter replacement price: "))
        if quantity < 0 or price <= 0:
            print("Quantity and price must be positive.")
            return
    except ValueError:
        print("Invalid input. Use numbers for year, quantity and price.")
        return

    catalog.append({"title": title, "author": author, "genre": genre,
                    "year": year, "quantity": quantity, "price": price})
    print("Book successfully registered.\n")

# Function to find and display book by title or author (case insensitive)
def search_book():
    query = input("Enter book title or author to search: ").strip().lower()
    found = False
    for book in catalog:
        if query in book["title"].lower() or query in book["author"].lower():
            display_book(book)
            found = True
    if not found:
        print("Book not found. Do you want to register it?")

# Display book details
def display_book(book):
    print("\n--- Book Details ---")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Genre: {book['genre']}")
    print(f"Year: {book['year']}")
    print(f"Quantity: {book['quantity']}")
    print(f"Replacement Price: {book['price']}\n")

# Function to update book quantity or price
def update_book():
    title = input("Enter the title of the book to update: ").strip().lower()
    for book in catalog:
        if book["title"].lower() == title:
            try:
                quantity = int(input("Enter new quantity: "))
                price = float(input("Enter new replacement price: "))
                if quantity < 0 or price <= 0:
                    print("Values must be positive.")
                    return
                book["quantity"] = quantity
                book["price"] = price
                print("Book updated successfully.\n")
                return
            except ValueError:
                print("Invalid input. Use valid numbers.")
                return
    print("Book not found.")

# Function to delete a book after confirmation
def delete_book():
    title = input("Enter the title of the book to delete: ").strip().lower()
    for book in catalog:
        if book["title"].lower() == title:
            confirm = input(f"Are you sure you want to delete '{book['title']}'? (y/n): ")
            if confirm.lower() == 'y':
                catalog.remove(book)
                print("Book successfully deleted.\n")
            else:
                print("Deletion cancelled.\n")
            return
    print("Book not found.\n")

# Function to generate reports
def generate_reports():
    total_value = sum(book['price'] * book['quantity'] for book in catalog)
    print(f"\nTotal inventory replacement value: {total_value:.2f}")

    genres = {}
    for book in catalog:
        genre = book['genre']
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(book)

    for genre, books in genres.items():
        oldest = min(books, key=lambda b: b['year'])
        newest = max(books, key=lambda b: b['year'])
        print(f"\nGenre: {genre}")
        print(f"  Oldest: {oldest['title']} ({oldest['year']})")
        print(f"  Newest: {newest['title']} ({newest['year']})")

# Menu interface for user interaction
def main():
    while True:
        print("\n--- Library Catalog Menu ---")
        print("1. Register new book")
        print("2. Search book")
        print("3. Update book info")
        print("4. Delete book")
        print("5. Generate reports")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            register_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            generate_reports()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
