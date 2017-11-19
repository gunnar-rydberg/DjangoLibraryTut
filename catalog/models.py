""" Models """
import uuid
from django.db import models
from django.urls import  reverse
from django.contrib.auth.models import User
from datetime import date


class Genre(models.Model):
    """ Book genre """
    name = models.CharField(max_length=200, help_text="Enter book genre")

    def __str__(self):
        return self.name


class Book(models.Model):
    """ Book representation """
    title = models.CharField(max_length=200)
    
    # Relation
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Enter brief description of the book")
    
    isbn = models.CharField('ISBN', max_length=13, help_text='13 character ISBN')
    
    # Relations
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    class Meta:
        ordering = ['title']

    def __str__(self):
        """ str() """
        return self.title

    def get_absolute_url(self):
        """ Returns detail view """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """ String rep of genres (max 3) """
        return ', '.join([genre.name for genre in self.genre.all()[:3] ])
    # As functions are objects themselfes I gues you can add properties to them...
    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """ Model of book instances, ie. individual books that exist in the library """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1 , choices=LOAN_STATUS, blank=True, default='m', help_text="Book availability")

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    class Meta:
        ordering = ['due_back'] #NOTE some framework automagic rely on this one

    def __str__(self):
        """ str() """
        return "{} ({})".format(self.id, self.book.title)

class Author(models.Model):
        """ Author model """
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField(null=True, blank=True)
        date_of_death = models.DateField('Died', null=True, blank=True)

        def get_absolute_url(self):
            """ Return detail author view """
            return reverse('author-detail', args=[str(self.id)])

        def __str__(self):
            """ str() """
            return "{}, {}".format(self.last_name, self.first_name)







