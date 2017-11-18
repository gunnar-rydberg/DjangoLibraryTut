from django.contrib import admin

from .models import Genre,Book,BookInstance,Author
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # Placing dates in the tuple makes them appear on the same row in the view
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # Don't add non-existing entries to the list !!! Why ?


#Decorator that applies the class to admin interface as 'admin.site.register(<model>,<admin.class>)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Select columns to show at admin site list. (display_genre is a method)
    list_display = ('title', 'author','display_genre')
    inlines = [BookInstanceInline]

    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Add filters to admin site
    list_filter = ('status' ,'due_back')

    fieldsets = (
        # Section 1 (no title)
        (None, {
            'fields': ('book','imprint','id')
        }),
        # Section 2 'Availability'
        ('Availability', {
            'fields': ('status', 'due_back')
        }),        
    )

admin.site.register(Genre)




