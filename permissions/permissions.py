from rest_framework.permissions import BasePermission

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
        return request.user.role == 'custom'

# Composite
class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['manager', 'admin']

class IsTeamLeadOrAbove(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['team_lead', 'manager', 'admin']

class IsAgentOrAbove(BasePermission):
    def has_permission(self, request, view):
        allowed_roles = ["agent", "manager", "admin", "team_lead"]  # add "custom" here
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.role.lower() in allowed_roles
        )