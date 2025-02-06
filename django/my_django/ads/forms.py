from django.forms import ModelForm, TextInput

from .models import Ad


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'disc',
            'image',
            'email',
            'category',
            'status',
        ]
        widgets = {
            'title':TextInput(attrs={
                'placeholder':"Заголовок",
                'maxLength':"32",
            }),
            'disc':TextInput(attrs={
                'placeholder':"Описание",
                'maxLength':"64",
            })
        }