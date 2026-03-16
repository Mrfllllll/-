from media import Movie
from series import Series


class Collection:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f'\n✓ Добавлено: "{item.title}"')

    def remove_by_title(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                self.items.remove(item)
                print(f'✓ Удалено: "{item.title}"')
                return
        print(f'✗ Не найдено: "{title}"')

    def search_by_title(self, query):
        query = query.lower()
        return [item for item in self.items if query in item.title.lower()]

    def search_by_genre(self, genre):
        genre = genre.lower()
        return [item for item in self.items if genre in item.genre.lower()]

    def sorted_by_rating(self, descending=True):
        return sorted(self.items, key=lambda x: x.rating, reverse=descending)

    def show_all(self):
        if not self.items:
            print("\nКоллекция пуста.")
            return
        print(f"\n══ Коллекция ({len(self.items)} шт.) ══")
        for i, item in enumerate(self.items, 1):
            print(f"  {i}. {item}")

    def show_details(self, title):
        results = self.search_by_title(title)
        if not results:
            print(f'✗ Не найдено: "{title}"')
            return
        for item in results:
            print("\n" + "─" * 35)
            print(item.info())
            print("─" * 35)


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Ошибка: введите целое число.")


def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0.0 <= value <= 10.0:
                return value
            print("  Ошибка: рейтинг должен быть от 0.0 до 10.0.")
        except ValueError:
            print("  Ошибка: введите число (например: 8.5).")


def print_menu():
    print("\n╔══════════════════════════════╗")
    print("║   Учёт фильмов и сериалов    ║")
    print("╠══════════════════════════════╣")
    print("║  1. Добавить фильм           ║")
    print("║  2. Добавить сериал          ║")
    print("║  3. Показать всю коллекцию   ║")
    print("║  4. Поиск по названию        ║")
    print("║  5. Поиск по жанру           ║")
    print("║  6. Сортировка по рейтингу   ║")
    print("║  7. Подробная информация     ║")
    print("║  8. Удалить по названию      ║")
    print("║  0. Выход                    ║")
    print("╚══════════════════════════════╝")


def add_movie(collection):
    print("\n── Новый фильм ──")
    title  = input("Название  : ").strip()
    year   = input_int("Год       : ")
    genre  = input("Жанр      : ").strip()
    rating = input_float("Рейтинг (0-10): ")
    collection.add(Movie(title, year, genre, rating))


def add_series(collection):
    print("\n── Новый сериал ──")
    title    = input("Название  : ").strip()
    year     = input_int("Год начала: ")
    genre    = input("Жанр      : ").strip()
    rating   = input_float("Рейтинг (0-10): ")
    seasons  = input_int("Сезонов   : ")
    episodes = input_int("Серий     : ")
    collection.add(Series(title, year, genre, rating, seasons, episodes))


def main():
    collection = Collection()

    collection.add(Movie("Интерстеллар", 2014, "Фантастика", 8.6))
    collection.add(Movie("Зелёная книга", 2018, "Драма", 8.2))
    collection.add(Series("Во все тяжкие", 2008, "Триллер", 9.5, 5, 62))
    collection.add(Series("Игра Престолов", 2011, "Фэнтези", 9.2, 8, 73))

    while True:
        print_menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            add_movie(collection)
        elif choice == "2":
            add_series(collection)
        elif choice == "3":
            collection.show_all()
        elif choice == "4":
            query = input("\nВведите название (или его часть): ").strip()
            results = collection.search_by_title(query)
            if results:
                print(f"\nНайдено ({len(results)}):")
                for item in results:
                    print(f"  • {item}")
            else:
                print("Ничего не найдено.")
        elif choice == "5":
            genre = input("\nВведите жанр: ").strip()
            results = collection.search_by_genre(genre)
            if results:
                print(f"\nНайдено ({len(results)}):")
                for item in results:
                    print(f"  • {item}")
            else:
                print("Ничего не найдено.")
        elif choice == "6":
            sorted_items = collection.sorted_by_rating()
            print("\n══ По рейтингу (убывание) ══")
            for i, item in enumerate(sorted_items, 1):
                print(f"  {i}. {item}")
        elif choice == "7":
            title = input("\nВведите название: ").strip()
            collection.show_details(title)
        elif choice == "8":
            title = input("\nВведите название для удаления: ").strip()
            collection.remove_by_title(title)
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
