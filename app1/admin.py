from django.contrib import admin
from .models import Registration

# Register your models here.

@admin.register(Registration)
class modelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "address",
        "street",
        "pincode",
        "image",
    )