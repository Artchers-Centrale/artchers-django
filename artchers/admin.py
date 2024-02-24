from django.contrib import admin

from .models import district, vote

admin.site.register(district)
admin.site.register(vote)