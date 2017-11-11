from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'user_last_name', 'user_email' )

    def user_name(self, obj):
        return obj.user.first_name

    user_name.short_description = 'imię'    

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = 'nazwisko'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'email'

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)


