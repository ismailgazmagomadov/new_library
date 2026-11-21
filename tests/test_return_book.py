from src.models.library import Library


def test_return_book():
    library = Library("Городская библиотека")
    library.add_book("Мастер и Маргарита", "Булгаков")
    library.borrow_book("Мастер и Маргарита")

    result = library.return_book("Мастер и Маргарита")

    assert "возвращена" in result


def test_find_book_ignore_case():
    library = Library("Городская библиотека")
    library.add_book("Мастер и Маргарита", "Булгаков")

    assert library.find_book("  мастер и маргарита ") is not None
