from django.forms import fields, ModelForm

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publication_date",
            "isbn_number",
            "number_of_pages",
            "cover_link",
            "publication_language",
        ]
