from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'), # pk is expected by generic views
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'), # pk is expected by generic views
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^librarian/$', views.LoanedBooksListView.as_view(), name='librarian-books'),
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]