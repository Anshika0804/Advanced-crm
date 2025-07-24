from django.contrib import admin
from .models import Lead
from contacts.models import Contact
from .models import Ticket, Attachment, Campaign, Note 

admin.site.register(Ticket)
admin.site.register(Attachment)
admin.site.register(Campaign)
admin.site.register(Note)

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0
    fields = ('first_name', 'email', 'phone', 'created_at')
    readonly_fields = ('created_at',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ['created_at']
    inlines = [ContactInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='agent').exists():
            return qs.filter(user=request.user)
        elif request.user.groups.filter(name='manager').exists():
            return qs  # Managers can see all
        elif request.user.groups.filter(name='admin').exists() or request.user.is_superuser:
            return qs
        return qs.none()

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='agent').exists():
            return obj is None or obj.user == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='agent').exists():
            return obj is None or obj.user == request.user
        return True

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
