from django.contrib import admin
from accomodation.models import Dinner

class DinnerModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'user_last_name', 'remark' )

    def user_name(self, obj):
        return obj.user.first_name

    user_name.short_description = 'imię'

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = 'nazwisko'

# Register your models here.
admin.site.register(Dinner, DinnerModelAdmin)

