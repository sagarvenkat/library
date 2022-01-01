from django.contrib import admin
from .models import Author,Genre,Book,BookInstance
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('second_name','first_name','dob','dod')

class BookAdmin(admin.ModelAdmin):
  list_display = ('title','author')

class BookInstanceAdmin(admin.ModelAdmin):
  pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookInstance)
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
