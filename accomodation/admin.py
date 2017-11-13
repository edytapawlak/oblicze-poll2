from django.contrib import admin
from accomodation.models import Dinner, Hostel 

class DinnerModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'user_name', 'user_last_name', 'remark' )

    def date(self, obj):
        return obj.confdate.date

    def user_name(self, obj):
        return obj.user.first_name

    user_name.short_description = 'imię'

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = 'nazwisko'

class HostelModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'user_name', 'user_last_name', 'hostel_name');

    def date(self, obj):
        return obj.confdate.date

    def user_name(self, obj):
        return obj.user.first_name

    user_name.short_description = 'imię'

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = 'nazwisko'

class ConfDayModelAdmin(admin.ModelAdmin):
    list_display = ('date', )

# Register your models here.
admin.site.register(Dinner, DinnerModelAdmin)
admin.site.register(Hostel, HostelModelAdmin)
