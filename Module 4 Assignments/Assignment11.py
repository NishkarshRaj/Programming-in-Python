#Assignment 11
class Book:
    def __init__(self,title,author,publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

def print_details(b):
    print("Book name:",b.title)
    print("Author:",b.author)
    print("Publisher:",b.publisher)

book1 = Book('Artificial Intelligence','Nishkarsh Raj','UPES')
book2 = Book('DevOps','Nishkarsh Raj','UPES')
book3 = Book('Big Data','Shubham Bansal','UPES')
book4 = Book('Cloud Computing','Karan Nautiyal','UPES')
book5 = Book('IOT','Vikrant Singh','UPES')

print_details(book1)
