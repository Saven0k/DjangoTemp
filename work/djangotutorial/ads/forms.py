from django.forms import ModelForm, TextInput, EmailInput
from .models import Ad

class AdsForms(ModelForm):
    class Meta:
        model = Ad
        fields = [
            'title',
            'discription',
            'img',
            'email',
            'status',    
            'categories',
        ]
        
        widgets = {
            'title': TextInput(attrs = {
                'class': 'title_input',
                'placeholder':'Заголовок объявления',
                'maxlength':'32'
            }),
            'discription': TextInput(attrs = {
                'class': 'discription_input',
                'placeholder':'Описание объявления',    
                'maxlength':'64'
            }),
            'email':EmailInput(attrs = {
                'class': 'discription_input',
                'placeholder':'Email автора',
            }),            
        }