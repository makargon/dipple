from django.contrib import admin
from .models import News, Comments, Tags
# Register your models here.

admin.site.register(News)

admin.site.register(Comments)
admin.site.register(Tags)