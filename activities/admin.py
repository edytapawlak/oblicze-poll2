from django.contrib import admin
from activities.models import Poster, Lecture, Author, Tag, Break

class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstract' )

class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstract' )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'author', 'lecture_title', 'poster_title', )
    
    def author(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def lecture_title(self, obj):
        if (obj.lecture_id is not None):
            return obj.lecture_id.title
    
    def poster_title(self, obj):
        if obj.poster_id is not None:
            return obj.poster_id.title

# Register your models here.
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Break)
