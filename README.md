### Метод `add_new_book`

**Тесты:**
- `test_add_new_book_add_two_books` — добавление двух книг  
- `test_add_new_book_valid_title` — добавление книг с валидным названием  
- `test_add_new_book_invalid_title` — попытка добавить книги с невалидным названием  
- `test_add_new_book_duplicated_book` — добавление дубликата книги  

---

### Метод `set_book_genre`

**Тесты:**
- `test_set_book_genre_book_and_genre_exist` — установка жанра для существующей книги  
- `test_set_book_genre_book_nonexistent` — установка жанра для несуществующей книги  
- `test_set_book_genre_when_genre_nonexistent` — установка несуществующего жанра  

---

### Метод `get_book_genre`

**Тесты:**
- `test_get_book_genre_existent_book` — получение жанра для книги с установленным жанром  
- `test_get_book_genre_nonexistent_book` — получение жанра для несуществующей книги  
- `test_get_book_genre_existent_book_without_genre` — получение жанра для книги без жанра  

---

### Метод `get_books_with_specific_genre`

**Тесты:**
- `test_get_books_with_specific_single_book` — получение одной книги по конкретному жанру  
- `test_get_books_with_specific_genre_multiple_books` — получение нескольких книг по конкретному жанру  
- `test_get_books_with_specific_invalid_genre` — запрос книг с несуществующим жанром  
- `test_get_books_with_specific_genre_without_books` — запрос книг по жанру, которому ещё не назначено книг  

---

### Метод `get_books_genre`

**Тесты:**
- `test_get_books_genre_get_books_dict` — получение словаря «книга:жанр»  

---

### Метод `get_books_for_children`

**Тесты:**
- `test_get_books_for_children_non_age_restricted_genres` — получение списка книг для детей  
- `test_get_books_for_children_age_restricted_genres` — проверка, что в_
