class Library:  
    
  
    def __init__(self, name, book_count, book_names):  
        self.name = name
        self.book_count = book_count
        self.book_names = book_names
    
    def __add__(self, book):

        new_count = self.book_count + 1
        self.book_names.append(book)

        return Library(name = self.name, book_count = new_count, book_names = self.book_names)
    
    
    def  __gt__(self, biblio2):
       
    
        if self.book_count > biblio2.book_count:
            return True
        else:
            return False
    
    def  __eq__(self, biblio2):
        
        
        if self.book_names == biblio2.book_names:
            return True
        else:
            return False
    
    def __repr__(self):
        return str(self.name)
    
    def __str__(self):
        return str(self.name)


        
        
class Book:  
     
    def __init__(self, name, author, year):  
        self.name = name  
        self.author = author
        self.year = year
    def __repr__(self):
        return str(self.name)
    
    def __str__(self):
        return str(self.name)

    
    def  __eq__(self, book2):
        
        
        if self.name == book2.name and self.author == book2.author:
            return True
        else:
            return False

 
book1 = Book(name="Теоретическая физика. Том 1. Механика", author="Ландау Л.Д., Лифшиц Е.М.", year=2004)
book2 = Book(name="Сборник еврейских анекдотов", author="Аркадий Хайт", year=2004)


biblio1 = Library(name="Библиотека МФТИ", book_count = 0, book_names = list())
biblio2 = Library(name="Ленинка", book_count = 0, book_names = list())

biblio1 = biblio1 + book1
biblio2 = biblio2 + book1
 
print(biblio1.book_count)

print(biblio1 > biblio2)
print(biblio1 == biblio2) 

biblio1 += book2
print(biblio1.book_count)

print(biblio1.book_names)

print(biblio1 > biblio2) 
print(biblio1 == biblio2) 
