class Books:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Availability: {self.availability}")

    def check_out(self):
        # Check if the book is available
        if self.availability.lower() == "yes":
            self.availability = "no"
            print(f"You have checked out '{self.title}'.")
        else:
            print(f"'{self.title}' is already checked out.")
            
all_books = []  # List to store all book instances

# Adding books outside the class
def add_book_to_collection():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    availability = input("Is the book available? (yes/no): ")
    new_book = Books(title, author, availability)
    all_books.append(new_book)

def check_out():
    title_to_check_out = input('Enter the title of the book to check out: ')
    for book in all_books:
        if book.title.lower() == title_to_check_out.lower():  # Find the book by title
            book.check_out()
            break
    else:
        print("This title is not in the collection.")



while True:    
    request_add = input('Would you like to add a book to the collection? (yes/no) ')
    if request_add.lower() == 'yes':
        add_book_to_collection()
    else:
        request_check_out = input('Would you like to check out a book? (yes/no) ')
        if request_check_out.lower() == 'yes':
            check_out()
        else:
            print("No action taken.")
            break


for book in all_books:
    book.display_info()

