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
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_get_book_genre_one_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_book_genre_non_existent_book_returns_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_with_specific_genre_add_list_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Дюна' in books

    def test_get_books_for_children_add_only_children(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert 'Шрек' in children_books

    def test_get_books_for_children_age_rating_books_excluded(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Оно' not in children_books

    def test_add_book_in_favorites_not_in_collector_ignored(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_duplicate_ignored(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books().count('Дюна') == 1
        
    def test_delete_book_from_favorites_remove_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        'book_name, should_be_added',
        [
            ('', False),
            ('B' * 40, True),
            ('B' * 41, False)
        ]
    )
    def test_add_new_book_length_boundaries(self, book_name, should_be_added):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        is_added = book_name in collector.get_books_genre()
        assert is_added == should_be_added