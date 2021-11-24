class Film:  
     
  
    def __init__(self, name, director, year, country, duration, age_rating):  
        self.name = name  
        self.director = director
        self.year = year 
        self.country = country 
        self.duration = duration 
        self.age_rating = age_rating
        
    def is_allowed(self, man):
        
        if (2021 - man.year)  >= self.age_rating:
            return 'allowed'
        else:
            return 'not allowed'
        
class Cartoon(Film):
    
    def __init__(self, name, director, year, country, duration, age_rating, technique):
        super().__init__(self, name, director, year, country, duration, age_rating)
        
        self.technique = technique
    
    

class Anime(Cartoon):
   

    def __init__(self, name, director, year, duration, age_rating, technique):
        super().__init__(self, name, director, year, duration, age_rating)
        
        self.country = 'Japan'

class Human:  
     
        
    def __init__(self, name, sex, year):  
        self.name = name  
        self.sex = sex
        self.year = year 
            
movie = Film(name="Dune", director="Denis Villeneuve", year=2021,
  country="USA", duration=155, age_rating=13)            

man = Human(name="Neo", sex="M", year=1964)
print(movie.is_allowed(man)) 

        
