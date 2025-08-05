from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'lead']
  

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='agent').exists():
            return qs.filter(user=request.user)
        elif request.user.groups.filter(name='manager').exists():
            return qs
        elif request.user.groups.filter(name='admin').exists() or request.user.is_superuser:
            return qs
        return qs.none()


admin.site.register(Contact, ContactAdmin)