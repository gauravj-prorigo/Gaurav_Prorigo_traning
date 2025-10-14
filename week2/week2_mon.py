class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_det(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year}")


book1 = Book("Shyamchi Aai", "Sane Guruji", 1988)
book2 = Book("Yayati", "V. S. Khandeka", 1959)
book3 = Book("Mrutyunjay", "Shivaji Sawant", 1967)

book1.display_det()
print()
book2.display_det()
print()
book3.display_det()
