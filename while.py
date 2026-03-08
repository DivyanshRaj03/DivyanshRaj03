class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("----------------------")


# Creating book objects
book1 = Book("The Alchemist", "Paulo Coelho", 399)
book2 = Book("Python Programming", "John Zelle", 550)
book3 = Book("Wings of Fire", "A.P.J. Abdul Kalam", 450)

# Displaying book details
book1.display_details()
book2.display_details()
book3.display_details()
