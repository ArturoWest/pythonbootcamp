from django.contrib import admin
from maths.models import Math
# Register your models here.

class MathAdmin(admin.ModelAdmin):
    list_display = ["operation", "arg_a", "arg_b"]

admin.site.register(Math, MathAdmin)