from django.db import models
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import pre_delete

# Create your models here.


class Ad(models.Model):
    title = models.CharField("Заголовок", max_length=32)
    disc = models.CharField("Описание", max_length=64)
    email = models.EmailField("Email", max_length=32)
    image = models.ImageField("Image",upload_to='images/', default='images/default.png', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg'])
    ], blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField( "Category", related_name='ads' ,blank=True)   
    
    
    def get_absolute_url(self):
        return '/ads'
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    title = models.CharField('Заголовок', max_length=32)
    
    def __str__(self):
        return self.title
    
    
@receiver(pre_delete, sender=Category)
def delete(instance, **kwargs):
    ads = instance.ads.all()
    ads.delete()