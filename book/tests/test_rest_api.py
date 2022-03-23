from datetime import datetime

from rest_framework.test import APIClient

from ..models import Book

BOOK_LIST_URL = "/api/list/"


def create_test_book_objects() -> None:
    Book.objects.create(title="Hobbit", author="Tolkien")
    Book.objects.create(title="Python", author="John Smith")
    Book.objects.create(title="Django", author="Johnny Depp")


def test_get_book_list_returs_book_with_details(db):
    Book.objects.create(
        title="Hobbit",
        author="Tolkien",
        publication_date=datetime(2001, 2, 4),
        isbn_number=1234567890,
        number_of_pages=500,
        cover_link="http://hobbit-cover.jpg",
        publication_language="en",
    )
    api_client = APIClient()
    response = api_client.get(BOOK_LIST_URL)
    assert response.status_code == 200
    book_data = response.json()[0]
    assert book_data["title"] == "Hobbit"
    assert book_data["author"] == "Tolkien"
    assert book_data["publication_date"] == "2001-02-04"
    assert book_data["isbn_number"] == 1234567890
    assert book_data["cover_link"] == "http://hobbit-cover.jpg"
    assert book_data["publication_language"] == "en"


def test_get_book_list_returs_multiple_books(db):
    create_test_book_objects()
    api_client = APIClient()
    response = api_client.get(BOOK_LIST_URL)
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_book_list_returs_books_filter_by_title(db):
    create_test_book_objects()
    api_client = APIClient()
    response = api_client.get(f"{BOOK_LIST_URL}?search=hobbit")
    assert response.status_code == 200
    assert len(response.json()) == 1
    book_data = response.json()[0]
    assert book_data["title"] == "Hobbit"
    assert book_data["author"] == "Tolkien"


def test_get_book_list_returs_books_filter_by_author(db):
    create_test_book_objects()
    api_client = APIClient()
    response = api_client.get(f"{BOOK_LIST_URL}?search=tolkien")
    assert response.status_code == 200
    assert len(response.json()) == 1
    book_data = response.json()[0]
    assert book_data["title"] == "Hobbit"
    assert book_data["author"] == "Tolkien"
