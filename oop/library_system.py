class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
         pass

class EBook(Book):
        def __init__(self, title, author, file_size):
            super().__init__(title, author)
            self.file_size = file_size


class PrintBook(Book):
     def __init__(self, title, author, page_count):
          super().__init__(title, author)
          self.page_count = page_count


class Library:
    def __init__(self, book):
        self.book = book
    
    def add_book(self, book):
        self.books = []
        self.append(self.book)

    def list_books(self):
        print(self)

          
# class Car:
#   def __init__(self, engine):
#     self.engine = engine  # Engine object as an attribute

#   def start(self):
#     self.engine.start()

# class Engine:
#   def start(self):
#     print("Engine starting...")

# car = Car(Engine())
# car.start()  # Output: Engine starting...



# class Duck:  
#    def swim(self):  
#          print("I'm a duck, and I can swim.")  
   
# class Sparrow:  
#      def swim(self):  
#          print("I'm a sparrow, and I can swim.")  
   
# class Crocodile:  
#      def swim_walk(self):  
#          print("I'm a Crocodile, and I can swim, but not quack.")  
   
# def duck_testing(animal):  
#      animal.swim()  
       
       
# duck_testing(Duck())  
# duck_testing(Sparrow())  
# duck_testing(Crocodile())  






# class Component: 
  
#    # composite class constructor 
#     def __init__(self): 
#         print('Component class object created...') 
  
#     # composite class instance method 
#     def m1(self): 
#         print('Component class m1() method executed...') 
  
  
# class Composite: 
  
#     # composite class constructor 
#     def __init__(self): 
  
#         # creating object of component class 
#         self.obj1 = Component() 
          
#         print('Composite class object also created...') 
  
#      # composite class instance method 
#     def m2(self): 
        
#         print('Composite class m2() method executed...') 
  
#         # calling m1() method of component class 
#         self.obj1.m1() 
  
  
# # creating object of composite class 
# obj2 = Composite() 
  
# # calling m2() method of composite class 
# obj2.m2() 
# Output