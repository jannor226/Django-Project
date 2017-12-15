from django.contrib import admin
from .models import RegisterForm
from .forms import RegisterFormUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = RegisterFormUp

# Register your models here.
admin.site.register(RegisterForm)
