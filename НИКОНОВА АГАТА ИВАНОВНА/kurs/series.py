from media import Movie


class Series(Movie):

    def __init__(self, title, year, genre, rating, seasons, episodes):
        super().__init__(title, year, genre, rating)
        self.seasons = seasons
        self.episodes = episodes

    def info(self):
        base = super().info().replace("Фильм    :", "Сериал   :")
        return (
            base + "\n"
            f"Сезонов  : {self.seasons}\n"
            f"Серий    : {self.episodes}"
        )

    def __str__(self):
        return (
            f"[Сериал] {self.title} ({self.year}) | {self.genre} | "
            f"★ {self.rating:.1f} | {self.seasons} сез. / {self.episodes} эп."
        )
