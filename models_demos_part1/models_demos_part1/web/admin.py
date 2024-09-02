from django.contrib import admin

from models_demos_part1.web.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
