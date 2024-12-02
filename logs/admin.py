# Register your models here.
from django.contrib import admin
from .models import UserActivityLog

@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'timestamp', 'ip_address')
    list_filter = ('user', 'timestamp')
