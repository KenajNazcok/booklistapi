from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.all_books, name="all_books"),
    path("add/", views.add_book, name="add_book"),
    path("edit/<int:id>/", views.edit_book, name="edit_book"),
    path("delete/<int:id>/", views.delete_book, name="delete_book"),
    path("searched_data/", views.searched_data, name="searched_data"),
    path("api/list/", views.BookListAPIView.as_view(), name="api_list"),
    path("api_auth/", include("rest_framework.urls")),
    path("book_downloader/", views.book_downloader, name="book_downloader"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
