i

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
        assert collector.favorites.count('Война и мир') == 1

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
        assert len(collector.favorites) == 1

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
        assert 'Новая книга' not in collector.favorites

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []