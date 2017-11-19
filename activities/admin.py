from django.contrib import admin
from activities.models import Poster, Lecture, Author

# Register your models here.
admin.site.register(Lecture)
admin.site.register(Poster)
admin.site.register(Author)
