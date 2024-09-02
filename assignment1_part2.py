#assignment1_part2

class book: # we will be creating a class that is called book.
    author = ''
    title = '' # these are the two artibutes which is the author and the title

    def __init__(self, author='', title=''): # using an __init__ basically what we are doing is taking one argument to another argument
        self.author = author
        self.title = title 

    def display(self): # we are using the method display to put the title  and with the self method we are basically calling the object 
        print (f"{self.title}, written by {self.author}")

book1 = book('J.K Rowling', 'Harry Potter and the Goblet of Fire')
book2 = book('Walter Scott', 'Ivanhoe: A Romance')

book1.display()
book2.display()
