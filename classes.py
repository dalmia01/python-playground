class Library:
    def __init__(self):
        self.books = []
        
    @property
    def no_of_books(self):
        return len(self.books)
    
    def addBook(self, name, pages):
        self.books.append({
            "name" : name,
            "pages": pages
        })
    
    def printBooks(self):
        if self.no_of_books > 0:
            print("-----")
            print("All the books: ")
            for book in self.books:
                print(f"The book name is {book['name']} and have {book['pages']} pages")
        else:
            print("No books")

lib = Library()

def getInputs():
    bookName = input("Enter a book name: ")
    bookPages = 0
    try:
        bookPages = int(input("Enter pages in a book: "))
    except ValueError as err:
        print("error is :- ", err)
    
    lib.addBook(bookName, bookPages)

while True:
    isProceed = input("Do you want to proceed(Y/N): ")
    if(isProceed.lower() == "y"):
        getInputs()
    else:
        break
    
lib.printBooks()
    
