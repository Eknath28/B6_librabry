from django.contrib import admin
from .models import Book
# Register your models here.
print("admin.py")
admin.site.register(Book)
