from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import CustomUser

admin.site.unregister(Group)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('email', 'name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Group Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Team Info', {'fields': ('team',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'role', 'password1', 'password2')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
