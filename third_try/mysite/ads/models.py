from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.core.validators import FileExtensionValidator


class Ad(models.Model):
    title = models.CharField("Заголовок", max_length=32)
    disc = models.CharField("Описание", max_length=64)
    email = models.EmailField("Email")
    image = models.ImageField("Фотка", upload_to="images/", default='images/default.png', blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg'])
    ])
    status = models.BooleanField("Статус", default=False)
    category = models.ManyToManyField('Category', related_name='ads' , blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/ads'
    
    
    
class Category(models.Model):
    title = models.CharField('Заголовок', max_length=32)
    
    def __str__(self):
        return self.title
    
@receiver(pre_delete, sender=Category)
def delete(instance, **kwargs):
    ads = instance.ads.all()
    ads.delete()
