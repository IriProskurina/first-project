import pytest

from main import BooksCollector  # Убедитесь, что путь к вашему классу BooksCollector верен


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name', ['a' * 41, ''])
    def test_add_new_book_incorrect_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_book_exists_genre_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_get_book_genre_book_not_exists(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_new_book('Метро 2033')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Война и мир', 'Метро 2033']

    def test_get_books_for_children_age_rating_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Ужасы')  # Ужасы в genre_age_rating
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.favorites

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_copy(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        favorites_list = collector.get_list_of_favorites_books()
        favorites_list.append('Новая книга')  # Попытка изменить возвращённый список
        assert 'Новая книга' not in collector.favorites  # Проверка, что favorites не изменился