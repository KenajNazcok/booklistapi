from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

import requests

from .forms import BookForm
from .models import Book
from .serializer import BookSerializer
from .utils import read_date


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ["author", "title", "publication_language"]


def all_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


@login_required
def add_book(request):
    form = BookForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_books)

    return render(request, "book_form.html", {"form": form})


@login_required
def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect(all_books)

    return render(request, "book_form.html", {"form": form})


@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == "POST":
        book.delete()
        return redirect(all_books)

    return render(request, "submit_to_delete.html", {"book": book})


def searched_data(request):
    if request.method == "POST" and "searched" in request.POST:
        searched = request.POST["searched"]
        qs = (
            Q(author__contains=searched)
            | Q(title__contains=searched)
            | Q(publication_language__contains=searched)
        )
        data = Book.objects.filter(qs)
        return render(
            request,
            "searched_data.html",
            {"searched": searched, "books": data},
        )
    else:
        displaydata = Book.objects.all()
        return render(request, "books.html", {"books": displaydata})


@login_required
def book_downloader(request):
    search = request.POST["search"]

    if not search:
        return redirect("/books/all/")

    params = {"q": search}
    response: requests.Response = requests.get(
        "https://www.googleapis.com/books/v1/volumes", params=params
    )
    data = response.json()

    books = []
    for book in data["items"]:
        book_data = book["volumeInfo"]
        isbn_number = None
        for iid in book_data.get("industryIdentifiers", []):
            if iid["type"] == "ISBN_13":
                isbn_number = iid["iden tifier"]
                break
            elif iid["type"] == "ISBN_10":
                isbn_number = iid["identifier"]

        title = book_data["title"]
        author = ", ".join(book_data.get("authors", ""))

        defaults = {
            "publication_date": read_date(book_data.get("publishedDate", "")),
            "isbn_number": isbn_number,
            "number_of_pages": book_data.get("pageCount"),
            "cover_link": book_data.get("imageLinks", {}).get("thumbnail", ""),
            "publication_language": book_data.get("language", ""),
        }
        book, _ = Book.objects.get_or_create(
            title=title, author=author, defaults=defaults
        )
        books.append(book)

    return render(request, "book_downloader.html", {"books": books})
