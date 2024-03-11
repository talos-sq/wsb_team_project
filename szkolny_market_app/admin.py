from django.contrib import admin
from .models import *

admin.site.site_header = "Sklepikowy panel administracyjny"
admin.site.site_title = "Sklepikowy panel administracyjny"


@admin.register(Product)
class AbilityAdmin(admin.ModelAdmin):
    model = Product

    list_display = []
