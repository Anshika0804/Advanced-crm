from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'member_count', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
