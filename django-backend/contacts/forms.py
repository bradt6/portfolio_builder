from django.forms import ModelForm, Textarea
from .models import Contact

class ContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'description_of_job': Textarea(attrs={'cols': 80, 'rows': 20}),
        }