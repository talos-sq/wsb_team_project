from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

admin.site.site_header = "Sklepikowy panel administracyjny"
admin.site.site_title = "Sklepikowy panel administracyjny"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ["user", "balance"]


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    model = Parent
    list_display = ["user"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "quantity", "category", "description"]


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CustomPermissionInline(admin.StackedInline):
    model = UserCustomPermissions
    can_delete = False


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [CustomPermissionInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
