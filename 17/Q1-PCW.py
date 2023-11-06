class Media:
    def __init__(self, title, author_director, rating):
        self.title = title
        self.author_director = author_director
        self.rating = rating

    def summary(self):
        return f"This is a media item titled {self.title}."

    def ratingInfo(self):
        return f"Rated {self.rating}."


class Book(Media):
    def __init__(self, title, author, rating, pages):
        super().__init__(title, author, rating)
        self.pages = pages

    def summary(self):
        return f"This is a book titled {self.title} by {self.author_director}."

    def ratingInfo(self):
        return f"Reader's rating: {self.rating}."


class Movie(Media):
    def __init__(self, title, director, rating, duration):
        super().__init__(title, director, rating)
        self.duration = duration

    def summary(self):
        return f"This is a movie titled {self.title} directed by {self.author_director}."

    def ratingInfo(self):
        return f"Viewer's rating: {self.rating}."


class Fiction(Book):
    def __init__(self, title, author, rating, pages, genre):
        super().__init__(title, author, rating, pages)
        self.genre = genre

    def summary(self):
        return f"This is a fiction book titled {self.title} in the {self.genre} genre."


class NonFiction(Book):
    def __init__(self, title, author, rating, pages, subject):
        super().__init__(title, author, rating, pages)
        self.subject = subject

    def summary(self):
        return f"This is a non-fiction book titled {self.title} about {self.subject}."


class Action(Movie):
    def __init__(self, title, director, rating, duration, hero):
        super().__init__(title, director, rating, duration)
        self.hero = hero

    def summary(self):
        return f"This is an action movie featuring {self.hero}."


class Comedy(Movie):
    def __init__(self, title, director, rating, duration, humor_type):
        super().__init__(title, director, rating, duration)
        self.humor_type = humor_type

    def summary(self):
        return f"This is a comedy movie with {self.humor_type} humor."


# Example usage
media1 = Media("Generic Media", "John Doe", "5 Stars")
print(media1.summary())
print(media1.ratingInfo())

book1 = Fiction("Harry Potter", "J.K. Rowling", "5 Stars", 400, "Fantasy")
print(book1.summary())
print(book1.ratingInfo())

movie1 = Action("Die Hard", "John McTiernan",
                "4.5 Stars", "2h 12m", "John McClane")
print(movie1.summary())
print(movie1.ratingInfo())
