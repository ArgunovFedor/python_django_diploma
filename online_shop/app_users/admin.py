from app_users.models import UserProfile
from django.contrib import admin


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id']


admin.site.register(UserProfile, UserProfileAdmin)
