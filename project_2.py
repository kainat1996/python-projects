# make a library system where a student can borrow a book from the list of books.abs
# create a separate library and student class .abs
# progeram must be menu driven
# you can use any methods and attributes.

# so for this we are going to make two sepaate classes of students and library
# and pass 4 different instance attributes                                                                                                                    
class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks  #pass self parameter because it is autometically pass when the object is called

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName) # this will remove the book which has been borrowed by someone 
            return True # else clause is the none path, so we need to return the value 
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName) # it will add the book back to the library
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__": #the module that is being run is the main program.
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"]) #the books we have in library
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True): #it will run the set of statements
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: ")) # it will allow the user to enter his choice
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
