from django.contrib import admin
from .models import Lead
from contacts.models import Contact
from .models import Ticket, Attachment, Campaign, Note 

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description') 

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_by')

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at', 'ticket') 


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0
    fields = ('name', 'email', 'phone_number', 'created_at')
    readonly_fields = ('created_at',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at', 'assigned_to', 'get_user_name')
    search_fields = ('name', 'email')
    list_filter = ['created_at']
    inlines = [ContactInline]


    def get_user_name(self, obj):
        return obj.user.name if obj.user else "-"
    get_user_name.short_description = 'Assigned by'


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        print("Logged in as:", request.user.email)
        print("User groups:", list(request.user.groups.values_list('name', flat=True)))
        
        if request.user.groups.filter(name__iexact='agent').exists():
            return qs.filter(user=request.user)
        elif request.user.groups.filter(name__iexact='manager').exists():
            return qs
        elif request.user.groups.filter(name__iexact='admin').exists() or request.user.is_superuser:
            return qs
        else:
            qs = qs.none()
        
        print("Queryset for current user:", qs)
        return qs


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
