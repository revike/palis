from django.contrib import admin

from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'telegram_id', 'username', 'email', 'first_name', 'last_name')
    list_display_links = (
        'id', 'telegram_id', 'username', 'email', 'first_name', 'last_name')
    fields = (
        'id', 'telegram_id', 'username', 'email', 'first_name', 'last_name',
        'is_active', 'is_staff', 'is_superuser', 'date_joined',)
    readonly_fields = ('id', 'telegram_id', 'username', 'date_joined',)


admin.site.register(User, UserAdmin)
admin.site.site_header = 'Админ-панель'
