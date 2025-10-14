class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_det(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year}")


class DigitalBook(Book):
    def __init__(self, title, author, year,pages):
        super().__init__(title, author, year)
        self.pages = pages
        
    def display_det(self):
        super().display_det()
        print("total page is :",self.pages)
    
book1 = DigitalBook("Shyamchi Aai", "Sane Guruji", 1988,250)
book2 = DigitalBook("Yayati", "V. S. Khandeka", 1959,500)
book3 = DigitalBook("Mrutyunjay", "Shivaji Sawant", 1967,133)

book1.display_det()
print()
book2.display_det()
print()
book3.display_det()