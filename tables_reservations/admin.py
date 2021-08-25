from django.contrib import admin
from tables_reservations.models import Table

class TableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Table, TableAdmin)
# Register your models here.
