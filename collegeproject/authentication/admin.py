from django.contrib import admin
from . models import Department,Purpose
from . models import Course


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Department, DepartmentAdmin)



    





