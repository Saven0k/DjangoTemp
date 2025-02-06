from django.forms import ModelForm, TextInput, EmailInput

from .models import  Ad
class AdForm(ModelForm):
    class Meta:
        model= Ad
        fields = [
            'title',
            'disc',
            'email',
            'category',
            'img'
        ]
        widgets = {
            'title': TextInput(attrs={
                'maxLength':'32',
                'placeholder':'Заголовок',
            }),
            'disc': TextInput(attrs={
                'maxLength':'64',
                'placeholder':'Описание',
            }),
            'email':EmailInput(attrs={
                'maxLength': '32',
                'placeholder':'Email'
            })
        }
