from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "publication_date",
        "isbn_number",
        "number_of_pages",
        "cover_link",
        "publication_language",
    ]
    list_filter = ("publication_date",)
    search_fields = [
        "title",
        "author",
        "publication_language",
        "publication_date",
    ]
