from django.urls import path
from .views import BookListView , BookDetailView , AuthorListView
# from .views import books_list



urlpatterns = [
    path('list/', BookListView.as_view(), name='books_list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    
]
