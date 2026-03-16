class Movie:

    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating

    def info(self):
        return (
            f"Фильм    : {self.title}\n"
            f"Год      : {self.year}\n"
            f"Жанр     : {self.genre}\n"
            f"Рейтинг  : {self.rating:.1f}"
        )

    def __str__(self):
        return f"[Фильм] {self.title} ({self.year}) | {self.genre} | ★ {self.rating:.1f}"
