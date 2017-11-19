from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

#from django.contrib.auth.decorators import login_required
#@login_required
def index(request):
    """ home page of site """

    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()

    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count() # implicit all()

    # Visit counter using sessions
    # Use sessions to keep track of individual anonymous users (using cookies)
    # By default session data is stored on the DB (default cookie life is 2 weeks)
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_books':num_books, 
                 'num_instance':num_instances, 
                 'num_instances_available':num_instances_available,
                 'num_authors':num_authors,
                 'num_visits':num_visits},)

from django.views import generic

class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


#from django.contrib.auth.mixins import LoginRequiredMixin
#class BookListView(LoginRequiredMixin, generic.ListView):
#    pass
#    ...


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

from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """ List loaned books by current user """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        print("QUERY")
        return BookInstance.objects.filter(borrower=self.request.user) \
                                   .filter(status__exact='o') \
                                   .order_by('due_back')
                            
