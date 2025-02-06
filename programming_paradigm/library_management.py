class Book:
    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

    
    def return_book(self):
        # self._is_checked_out.append(title)
        self._book += 1
        # return True


        
class Library:
    def __init__(self):
        self._book = book
        pass

    def add_book(self):
        self._book.append(book)



        pass
        
            
    def check_out_book(self, title):
        self._is_checked_out.remove(title)
        self._book -= 1
        pass
    
    def return_book(self):
        # self._is_checked_out.append(title)
        self._book += 1
        # return True
        pass


    def list_available_books(self):
        print(f"weldone: {self.title}")


        pass