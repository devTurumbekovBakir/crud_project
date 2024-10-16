from django.contrib import admin

from .models import UserProfile, UserDetail, UserGroup

admin.site.register(UserProfile)
admin.site.register(UserDetail)
admin.site.register(UserGroup)
