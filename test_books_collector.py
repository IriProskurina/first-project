import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # add_new_book
    def test_add_new_book_success(self, collector):
        collector.add_new_book('Война и мир')
        assert 'Война и мир' in collector.books_genre

    def test_add_new_book_already_exists(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert list(collector.books_genre.keys()).count('Война и мир') == 1

    @pytest.mark.parametrize('name', ['a' * 41, ''])
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_name_is_none(self, collector):  # Дополнительный тест
        collector.add_new_book(None)  # Передаем None
        assert len(collector.books_genre) == 0

    # set_book_genre
    def test_set_book_genre_success(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_set_book_genre_book_not_exists(self, collector):
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_book_genre('Война и мир') is None

    def test_set_book_genre_genre_not_in_list(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Несуществующий жанр')
        assert collector.get_book_genre('Война и мир') == ''

    def test_set_book_genre_empty_genre(self, collector):  # Дополнительный тест
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', '') # Передаем пустую строку
        assert collector.get_book_genre('Война и мир') == ''

    # get_book_genre
    def test_get_book_genre_exists(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_get_book_genre_not_exists(self, collector):
        assert collector.get_book_genre('Война и мир') is None

    # get_books_with_specific_genre
    def test_get_books_with_specific_genre_exists(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_new_book('Метро 2033')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Война и мир', 'Метро 2033']

    def test_get_books_with_specific_genre_not_exists(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_with_specific_genre_empty_catalog(self, collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_genre_not_in_list(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        collector.genre = ['Ужасы', 'Детективы']
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_correct_output_order(self, collector): # Дополнительный тест
        collector.add_new_book('Книга A')
        collector.set_book_genre('Книга A', 'Фантастика')
        collector.add_new_book('Книга B')
        collector.set_book_genre('Книга B', 'Фантастика')
        collector.add_new_book('Книга C')
        collector.set_book_genre('Книга C', 'Детективы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга A', 'Книга B']

    # get_books_genre
    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book('Война и мир')
        assert type(collector.get_books_genre()) == dict

    def test_get_books_genre_returns_copy(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        before = collector.get_books_genre()
        before['Война и мир'] = 'Ужасы'
        assert collector.get_book_genre('Война и мир') == 'Фантастика'

    def test_get_books_genre_empty(self, collector):  # Дополнительный тест
        assert collector.get_books_genre() == {}

    # get_books_for_children
    def test_get_books_for_children_age_rating_exists(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Ужасы')  # Ужасы в genre_age_rating
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_genre_not_in_list(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_success(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Война и мир']

    def test_get_books_for_children_mixed_genres(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Война и мир']

    def test_get_books_for_children_empty_catalog(self, collector): # Дополнительный тест
        assert collector.get_books_for_children() == []

    # add_book_in_favorites
    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books_genre(self, collector):
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.favorites

    def test_add_book_in_favorites_already_added(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert collector.get_list_of_favorites_books().count('Война и мир') == 1

    # delete_book_from_favorites
    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Неизвестная книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_empty_favorites(self, collector):  # Дополнительный тест
        collector.delete_book_from_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == []

    # get_list_of_favorites_books
    def test_get_list_of_favorites_books_returns_list(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        assert type(collector.get_list_of_favorites_books()) == list

    def test_get_list_of_favorites_books_returns_copy(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        collector.add_book_in_favorites('Война и мир')
        before = collector.get_list_of_favorites_books()
        before.append('Новая книга')
        assert 'Новая книга' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_add_same_book_many_times_to_favorites(self, collector): # Дополнительный тест
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Фантастика')
        for _ in range(5):
            collector.add_book_in_favorites('Война и мир')
        assert collector.get_list_of_favorites_books().count('Война и мир') == 1