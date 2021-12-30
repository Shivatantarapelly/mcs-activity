from django.contrib import admin

# Register your models here.
from Book.models import BooksModel

admin.site.register(BooksModel)