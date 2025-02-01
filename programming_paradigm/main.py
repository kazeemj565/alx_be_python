# import sys
# from robust_division_calculator import safe_divide

# def main():
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <numerator> <denominator>")
#         sys.exit(1)

#     numerator = sys.argv[1]
#     denominator = sys.argv[2]

#     result = safe_divide(numerator, denominator)
#     print(result)

# if __name__ == "__main__":
#     main()
'''Your Book class should provide methods to check a book out and return it, 
affecting its availability.
Your Library class needs to manage a collection of books, 
including adding new books to the collection, 
checking a book out (which marks it as unavailable), 
returning it (making it available again), and listing all available books.
Implementing these functionalities requires careful thought 
about how objects interact with each other in terms of state and behavior.
Use the provided main.py for testing your implementation. 
The expected outputs give you a clear indication of how your program
 should behave if implemented correctly.'''

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()