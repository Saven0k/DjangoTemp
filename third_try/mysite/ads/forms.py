from .models import Ad
from django.forms import ModelForm, TextInput, EmailInput


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'disc',
            'image',
            'email',
            'status',
            'category'
        ]
        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Заголовок",
                'maxLength':"32"
            }),
            'disc': TextInput(attrs={
                'placeholder': "Основной текс",
                'maxLength':"64"
            }),
            'email': EmailInput(attrs={
                'placeholder': "email",
            })
        }