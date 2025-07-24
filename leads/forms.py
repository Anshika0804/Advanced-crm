# forms.py (in the same app as Lead)
from django import forms
from .models import Lead
from users.models import CustomUser

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        widgets = {
            'user': forms.Select()  # make sure it's a dropdown
        }

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user == '':  # if blank, treat as None
            return None
        return user
