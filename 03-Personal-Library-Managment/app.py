import json
import os

DATA_FILE = 'library.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(books):
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def add_book():
    print("\nAdd New Book")
    book = {
        'id': len(load_data()) + 1,
        'title': input("Title: "),
        'author': input("Author: "),
        'year': input("Publication Year: "),
        'genre': input("Genre: ")
    }
    books = load_data()
    books.append(book)
    save_data(books)
    print("\nBook added successfully!")

def list_books():
    books = load_data()
    print("\nBook List:")
    print("-" * 50)
    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year: {book['year']}")
        print(f"Genre: {book['genre']}")
        print("-" * 50)

def search_books():
    print("\nSearch Books")
    query = input("Search in title/author/genre: ").lower()
    results = []
    
    for book in load_data():
        if (query in book['title'].lower() or 
            query in book['author'].lower() or 
            query in book['genre'].lower()):
            results.append(book)
    
    if results:
        print(f"\nFound {len(results)} results:")
        for book in results:
            print(f"[{book['id']}] {book['title']} - {book['author']}")
    else:
        print("\nNo books found")

def update_book():
    book_id = int(input("\nEnter book ID to update: "))
    books = load_data()
    found = False
    
    for book in books:
        if book['id'] == book_id:
            print("\nEnter new data (press Enter to keep current value):")
            book['title'] = input(f"Title [{book['title']}]: ") or book['title']
            book['author'] = input(f"Author [{book['author']}]: ") or book['author']
            book['year'] = input(f"Year [{book['year']}]: ") or book['year']
            book['genre'] = input(f"Genre [{book['genre']}]: ") or book['genre']
            found = True
            break  
    
    if found:
        
        save_data(books)
        print("\nBook updated successfully!")
    else:
        print("\nBook not found")

def delete_book():
    book_id = int(input("\nEnter book ID to delete: "))
    books = load_data()
    new_books = [book for book in books if book['id'] != book_id]
    
    if len(new_books) != len(books):
        save_data(new_books)
        print("\nBook deleted successfully!")
    else:
        print("\nBook not found")

def show_menu():
    print("\n" + "="*30)
    print("My Personal Library")
    print("="*30)
    print("1. View all books")
    print("2. Add new book")
    print("3. Search books")
    print("4. Update book")
    print("5. Delete book")
    print("6. Exit")
    print("="*30)

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            list_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("\nThank you! Have a great day!")
            break
        else:
            print("\nInvalid choice! Please choose 1-6")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()