from django.forms import ModelForm
from .models import messages_contact

class messages_contact_form(ModelForm):
    class Meta:
        model = messages_contact
        fields = '__all__'
