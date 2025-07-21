class book:
    def __init__(self,title, author, year, status='available'):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        
    def display_info(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Status: {self.status}")

    def borrow(self):
        if self.status == 'available':
            self.status = 'borrowed'
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is currently not available for borrowing.")

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available.")

books_list = []

for i in range(3):
    print(f"\nEnter details for Book {i+1}:")
    title = input("Title: ")
    author = input("Author: ")
    
    try:
        year = int(input("Year of Publication: "))
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        continue

    book_instance = book(title, author, year)
    books_list.append(book_instance)

while True:
    print("\n--- Library Management ---")
    print("1. Display all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("\n--- Book Records ---")
        for book_instance in books_list:
            book_instance.display_info()
    
    elif choice == '2':
        title = input("Enter the title of the book to borrow: ")
        found = False
        for book_instance in books_list:
            if book_instance.title.lower() == title.lower():
                book_instance.borrow()
                found = True
                break
        if not found:
            print(f"Book '{title}' not found.")
    
    elif choice == '3':
        title = input("Enter the title of the book to return: ")
        found = False
        for book_instance in books_list:
            if book_instance.title.lower() == title.lower():
                book_instance.return_book()
                found = True
                break
        if not found:
            print(f"Book '{title}' not found.")
    
    elif choice == '4':
        print("Exiting the library management system.")
        break
    
    else:
        print("Invalid choice. Please try again.")