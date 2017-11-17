from django.contrib import admin

from .models import Genre,Book,BookInstance,Author
# Register your models here.

#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)


#admin.site.register(Book)
#admin.site.register(BookInstance)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','display_genre')
    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre)



