from django.contrib import admin

# Register your models here.

from .models import Username , Game , Property

admin.site.register(Username)
admin.site.register(Game)
admin.site.register(Property)
