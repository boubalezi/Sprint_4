Метод add_new_book
Тесты:
test_add_new_book_add_two_books - добавление двух книг
test_add_new_book_valid_title - добавление книг с валидным тайтлом
test_add_new_book_invalid_title - добавление книг с невалидным тайтлом
test_add_new_book_duplicated_book - добавление дубликата книги

Метод set_book_genre
Тесты:
test_set_book_genre_book_and_genre_exist - установка жанра для книги
test_set_book_genre_book_nonexistent - установка жанра для несуществующей книги
test_set_book_genre_when_genre_nonexistent - установка несуществующего жанра

Метод get_book_genre
Тесты:
test_get_book_genre_existent_book - получение жанра для существующей книги
test_get_book_genre_nonexistent_book - получение жанра для несуществующей книги
test_get_book_genre_existent_book_without_genre - получение жанра для книги без жанра

Метод get_books_with_specific_genre
Тесты:

test_get_books_with_specific_single_book - получение одной книги по конкретному жанру
test_get_books_with_specific_genre_multiple_books - получение нескольких книг по конкретному жанру
test_get_books_with_specific_invalid_genre - получение книг неизвестного жанра
test_get_books_with_specific_genre_without_books - получение книг для жанра, книг которого еще нет в списке

Метод get_books_genre
Тесты:
test_get_books_genre_get_books_dict - получение словаря книга:жанр

Метод get_books_for_children
Тесты:
test_get_books_for_children_non_age_restricted_genres - получение списка книг для детей
test_get_books_for_children_age_restricted_genres - проверка, книги не для детей не попадат в список детских
test_get_books_for_children_book_without_genre - проверка, что книги без жанра, не попадают в список детских книг

Метод add_book_in_favorites
Тесты:
ttest_add_book_in_favorites_two_existent_books - добавление существующих книг в избранное
test_add_book_in_favorites_non_existent_book - добавление несуществующих книг в избранное
test_add_book_in_favorites_book_duplicate - добавления дубликатов книг в избранное

Метод delete_book_from_favorites
Тесты:
test_delete_book_from_favorites_delete_one_book - удаление книги из избранного

Метод get_list_of_favorites
Тесты:
test_get_list_of_favorites_books_get_list - получение списка избранных книг
