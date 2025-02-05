from django.forms import ModelForm, TextInput, EmailInput

from .models import Ad

class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'discription',
            'email',
            'image',
            'categories',
            'status'
        ]
        widgets = {
            'title': TextInput(attrs={
                'placeholder':'Название',
                'class': 'title',
                'maxLength': 32,
            }),
            'discription': TextInput(attrs={
                'placeholder':'discription',
                'class': 'discription',
                'maxLength': 64,
            }),
            'email': EmailInput(attrs={
                'placeholder':'Email',
                'class': 'Email',
            })
        }