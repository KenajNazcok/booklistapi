from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(blank=True, null=True)
    isbn_number = models.PositiveBigIntegerField(
        blank=True, null=True, unique=True
    )
    number_of_pages = models.PositiveSmallIntegerField(blank=True, null=True)
    cover_link = models.URLField()
    publication_language = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"
