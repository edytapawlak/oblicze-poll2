from django.contrib import admin
from schedule.models import Date, Place, Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date', 'start', 'end', 'place', )

# Register your models here.
admin.site.register(Date)
admin.site.register(Place)
admin.site.register(Schedule, ScheduleAdmin)
