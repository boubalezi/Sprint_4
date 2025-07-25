import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        "book_title_valid",
        [
            "A",  # название из 1 символа
            "AB",  # название из 2 символов
            "Гордость и предубеждение и зомбииииии!!!",  # название из 40 символов
            "Гордость и предубеждение и зомбииииии!!",  # название из 39 символов
            "Гордость и предубеждение",  # название из 25 символов
        ],
    )
    def test_add_new_book_valid_title(self, collector, book_title_valid):
        collector.add_new_book(book_title_valid)

        assert book_title_valid in collector.books_genre

    @pytest.mark.parametrize(
        "book_title_invalid",
        [
            "",  # название из 0 символов
            "Гордость и предубеждение и зомбииииии!!!!",  # название из 41 символа
            "Гордость и предубеждение и зомбиииииии!!!!",  # название из 42 символа
            "Очень длинный тайтл" * 100,  # длинное название
        ],
    )
    def test_add_new_book_invalid_title(self, collector, book_title_invalid):
        collector.add_new_book(book_title_invalid)

        assert book_title_invalid not in collector.books_genre

    def test_add_new_book_duplicated_book(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Гордость и предубеждение и зомби")

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_book_and_genre_exist(self, collector):
        collector.add_new_book("Добро пожаловать в Зомбиленд")
        collector.set_book_genre("Добро пожаловать в Зомбиленд", "Комедии")

        assert collector.books_genre.get("Добро пожаловать в Зомбиленд") == "Комедии"

    def test_set_book_genre_book_nonexistent(self, collector):
        assert collector.books_genre.get("Добро пожаловать в Зомбиленд") == None

    def test_set_book_genre_when_genre_nonexistent(self, collector):
        collector.add_new_book("Добро пожаловать в Зомбиленд")
        collector.set_book_genre("Добро пожаловать в Зомбиленд", "Некомедии")

        assert collector.books_genre.get("Добро пожаловать в Зомбиленд") == ""

    def test_get_book_genre_existent_book(self, collector):
        collector.add_new_book("Алладин")
        collector.set_book_genre("Алладин", "Ужасы")

        assert collector.get_book_genre("Алладин") == "Ужасы"

    def test_get_book_genre_nonexistent_book(self, collector):
        collector.add_new_book("Алладин")
        collector.set_book_genre("Алладин", "Ужасы")

        assert collector.get_book_genre("Алладин и 101 ночь") == None

    def test_get_book_genre_existent_book_without_genre(self, collector):
        collector.add_new_book("Алиса в стране чудес")

        assert collector.get_book_genre("Алиса в стране чудес") == ""

    def test_get_books_with_specific_single_book(self, collector):
        collector.add_new_book("Ромео и Джульетта")
        collector.set_book_genre("Ромео и Джульетта", "Детективы")

        assert collector.get_books_with_specific_genre("Детективы") == [
            "Ромео и Джульетта"
        ]

    def test_get_books_with_specific_genre_multiple_books(self, collector):
        books = ["Том 1", "Том 2", "Том 3"]
        genre = "Ужасы"

        for item in books:
            collector.add_new_book(item)
            collector.set_book_genre(item, genre)

        assert set(collector.get_books_with_specific_genre(genre)) == set(books)

    def test_get_books_with_specific_invalid_genre(self, collector):
        collector.add_new_book("Белоснежка")
        collector.set_book_genre("Белоснежка", "Фантастика")

        assert collector.get_books_with_specific_genre("Неизвестный жанр") == []

    def test_get_books_with_specific_genre_without_books(self, collector):
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Комедии")

        assert collector.get_books_with_specific_genre("Фантастика") == []

    def test_get_books_genre_get_books_dict(self, collector):
        books = [("Том 1", "Ужасы"), ("Том 2", "Фантастика"), ("Том 3", "Детективы")]
        for book, genre in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert collector.get_books_genre() == {
            "Том 1": "Ужасы",
            "Том 2": "Фантастика",
            "Том 3": "Детективы",
        }

    def test_get_books_for_children_non_age_restricted_genres(self, collector):
        books = [
            ("Добро пожаловать в Зомбиленд", "Комедии"),
            ("100500 по Цельсию", "Фантастика"),
            ("Винни Пух", "Мультфильмы"),
        ]
        for book, genre in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == [
            "Добро пожаловать в Зомбиленд",
            "100500 по Цельсию",
            "Винни Пух",
        ]

    def test_get_books_for_children_age_restricted_genres(self, collector):
        collector.add_new_book("Белоснежка")
        collector.set_book_genre("Белоснежка", "Ужасы")
        collector.add_new_book("Белоснежка 2")
        collector.set_book_genre("Белоснежка 2", "Детективы")

        assert collector.get_books_for_children() == []

    def test_get_books_for_children_book_without_genre(self, collector):
        collector.add_new_book("Книга без жанра")
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_two_existent_books(self, collector):
        collector.add_new_book("Алладин")
        collector.add_book_in_favorites("Алладин")
        collector.add_new_book("1001 ночь")
        collector.add_book_in_favorites("1001 ночь")

        assert collector.favorites == ["Алладин", "1001 ночь"]

    def test_add_book_in_favorites_non_existent_book(self, collector):
        collector.add_new_book("Алладин")
        collector.add_book_in_favorites("Алладин и 1001 ночь")

        assert "Алладин и 1001 ночь" not in collector.favorites

    def test_add_book_in_favorites_book_duplicate(self, collector):
        collector.add_new_book("Алладин")
        collector.add_book_in_favorites("Алладин")
        collector.add_book_in_favorites("Алладин")

        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book("Алладин")
        collector.add_book_in_favorites("Алладин")
        collector.delete_book_from_favorites("Алладин")

        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_list(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        collector.add_book_in_favorites("Гордость и предубеждение и зомби")
        collector.add_book_in_favorites("Что делать, если ваш кот хочет вас убить")

        expected_result = [
            "Гордость и предубеждение и зомби",
            "Что делать, если ваш кот хочет вас убить",
        ]

        assert collector.get_list_of_favorites_books() == expected_result
