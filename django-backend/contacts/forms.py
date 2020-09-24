from django.forms import ModelForm, Textarea
from .models import Contact

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'description_of_job': Textarea(attrs={'cols': 80, 'rows': 20}),
        }