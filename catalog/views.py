from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):
    """ home page of site """

    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()

    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count() # implicit all()

    return render(
        request,
        'index.html',
        context={'num_books':num_books, 
                 'num_instance':num_instances, 
                 'num_instances_available':num_instances_available,
                 'num_authors':num_authors },)

from django.views import generic

class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1 #NOTE built in pagination
    
    #context_object_name = 'alternative_name'
    #queryset = Book.objects.filter(title__icontains='war')
    #template_name = 'books/alternative_list.html'

    # def get_queryset(self): ... return Book.objects.filter(...)
    # def get_context_data(self, **kwargs):  ... return context
            
class BookDetailView(generic.DetailView):
    model = Book


# def book_detail_view(request,pk):
#     try:
#         book_id=Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")

#     #book_id=get_object_or_404(Book, pk=pk)
    
#     return render(
#         request,
#         'catalog/book_detail.html',
#         context={'book':book_id,}
#     )

