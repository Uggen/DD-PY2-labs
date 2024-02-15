class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} by {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, Страницы: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом с плавающей запятой")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}, Продолжительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}', duration={self.duration})"


if __name__ == "__main__":
    book1 = PaperBook("Дубровский", "Пушкин А. С.", 180)
    book2 = AudioBook("Мы", "Замятин Е. И.", 10.5)

    print(book1)
    print(book2)

    try:
        book3 = PaperBook("Война и мир", "Лев Толстой", "1000")
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        book4 = AudioBook("Евгений Онегин", "Александр Пушкин", -9)
    except ValueError as e:
        print(f"Ошибка: {e}")
