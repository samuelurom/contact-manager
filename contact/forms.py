from .models import Contact
from django.forms import ModelForm, TextInput, EmailInput


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "phone"]

        widgets = {
            "first_name": TextInput(attrs={"class": "form-control mt-2 mb-3"}),
            "last_name": TextInput(attrs={"class": "form-control mt-2 mb-3"}),
            "email": EmailInput(attrs={"class": "form-control mt-2 mb-3"}),
            "phone": TextInput(attrs={"class": "form-control mt-2 mb-3"}),
        }
