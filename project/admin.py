from django.contrib import admin
from project.models import Account, Administrator, Client, Department, Employee, Incident, IncidentHistory

# Register your models here.
admin.site.register(Account)

admin.site.register(Administrator)

admin.site.register(Client)

admin.site.register(Department)

admin.site.register(Employee)

admin.site.register(Incident)

admin.site.register(IncidentHistory)
"""
class ChoiceInline(admin.TabularInline):
    model = Administrator
    extra = 3

class AdminInfo(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['fname']}),
        ('Date information', {'fields': ['fname'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('fname', 'pub_date', 'was_published_recently')
    list_filter = ['fname']
    search_fields = ['fname']

admin.site.register(Administrator, AdminInfo)

"""
