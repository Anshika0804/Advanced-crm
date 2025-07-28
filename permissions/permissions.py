from rest_framework.permissions import BasePermission
from users.models import CustomUser



class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role in ['manager', 'admin']

#General Role Checks.........
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'manager'

class IsTeamLead(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'team_lead'

class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'agent'

class IsCustomUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'custom_user'

# Composite Permissions.......
class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['manager', 'admin']

class IsTeamLeadOrAbove(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['team_lead', 'manager', 'admin']

class IsAgentOrAbove(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['agent', 'team_lead', 'manager', 'admin']


from rest_framework import permissions

# Can View Lead: Admins, Managers, Team Leads, OR the assigned user
class CanViewLead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.role in ['admin', 'manager', 'team_lead']
            or obj.user == request.user
        )


# Can Update Lead: Admins, Managers, Team Leads can update any, Custom Users only their own
class CanUpdateLead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ['admin', 'manager', 'team_lead']:
            return True
        return obj.user == request.user


# Can Delete Lead: Only Admins and Managers
class CanDeleteLead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role in ['admin', 'manager']


# Can Create Lead: Admins, Managers, Team Leads can create for anyone, Custom Users only for self
class CanCreateLead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['admin', 'manager', 'team_lead']:
            return True
        return request.method == "POST" and request.data.get("user") == str(request.user.id)
