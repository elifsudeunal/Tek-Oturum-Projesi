from django.contrib import admin
from .models import LoginLog, LogoutLog, FailedLoginLog

@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'user_agent', 'login_time', 'is_session_kicked')
    list_filter = ('user', 'login_time', 'ip_address', 'is_session_kicked')
    search_fields = ('user__username', 'ip_address', 'user_agent')

@admin.register(LogoutLog)
class LogoutLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'user_agent', 'logout_time')
    list_filter = ('user', 'logout_time', 'ip_address')
    search_fields = ('user__username', 'ip_address', 'user_agent')

@admin.register(FailedLoginLog)
class FailedLoginLogAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'timestamp')
    list_filter = ('timestamp', 'ip_address', 'username')
    search_fields = ('username',)
