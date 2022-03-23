import pdb

from django.test import Client
from django.urls import resolve, reverse

from pytest_django.asserts import assertTemplateUsed

from book.forms import BookForm
from book.models import Book
from book.views import (
    add_book,
    all_books,
    book_downloader,
    BookListAPIView,
    delete_book,
    edit_book,
    searched_data,
)


def test_missing_status_code():
    client = Client()
    response = client.get("/nothing")
    assert response.status_code == 404


def test_books_url_is_resolved():
    url = reverse("all_books")
    assert resolve(url).func == all_books


def test_books_url_is_resolved():
    url = reverse("add_book")
    assert resolve(url).func == add_book


def test_books_url_is_resolved():
    url = reverse("edit_book")
    assert resolve(url).func == edit_book


def test_books_url_is_resolved():
    url = reverse("delete_book")
    assert resolve(url).func == delete_book


def test_books_url_is_resolved():
    url = reverse("searched_data")
    assert resolve(url).func == searched_data


def test_books_url_is_resolved():
    url = reverse("api_list")
    assert resolve(url).func == BookListAPIView


def test_books_url_is_resolved():
    url = reverse("book_downloader")
    assert resolve(url).func == book_downloader


def test_book_model(db):

    book = Book.objects.create(
        title="mikołajek",
        author=["Rene Goscinny", "Jean Jacques Sempe "],
        publication_date="1960-01-01",
        isbn_number="9788420447865",
        number_of_pages="176",
        cover_link="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQNnnrnJQkHS3I8j9zQmAFBQ851znO-b_jDcJ7yrTEQ08iZ7BIE",
        publication_language="fr",
    )

    field_label = book._meta.get_field(
        "title",
    ).verbose_name
    field_label = book._meta.get_field(
        "author",
    ).verbose_name
    field_label = book._meta.get_field(
        "publication_date",
    ).verbose_name
    field_label = book._meta.get_field(
        "isbn_number",
    ).verbose_name
    field_label = book._meta.get_field(
        "number_of_pages",
    ).verbose_name
    field_label = book._meta.get_field(
        "cover_link",
    ).verbose_name
    field_label = book._meta.get_field(
        "publication_language",
    ).verbose_name
