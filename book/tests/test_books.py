from django.test import Client
from django.urls import resolve, reverse

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


def test_all_books_url_is_resolved():
    url = reverse("all_books")
    assert resolve(url).func == all_books


def test_add_book_url_is_resolved():
    url = reverse("add_book")
    assert resolve(url).func == add_book


def test_edit_book_url_is_resolved():
    url = reverse("edit_book")
    assert resolve(url).func == edit_book


def test_delete_book_url_is_resolved():
    url = reverse("delete_book")
    assert resolve(url).func == delete_book


def test_searched_data_url_is_resolved():
    url = reverse("searched_data")
    assert resolve(url).func == searched_data


def test_api_list_is_resolved():
    url = reverse("api_list")
    assert resolve(url).func == BookListAPIView


def test_book_downloader_is_resolved():
    url = reverse("book_downloader")
    assert resolve(url).func == book_downloader
