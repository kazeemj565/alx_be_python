class Book:

    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out


class Library:
    def __init__(self, is_checked_out, author, title, book):
        super().__init__(title, author, is_checked_out)
        self._book = book
        self._is_checked_out = is_checked_out
        pass

    def add_book(self, book):
        self._book.append(book)



        pass
        
            
    def check_out_book(self, title):
        self._is_checked_out.remove(title)
        self._book -= 1
        pass
    
    def return_book(self, title):
        self._is_checked_out.append(title)
        self._book += 1
        # return True
        pass


    def list_available_books(self):
        super().list_available_books()
        print(f"weldone: {self.title}")


        pass