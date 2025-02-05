from django.db import models
from django.db.models.signals import pre_delete
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver

# Create your models here.

class Ad(models.Model):
    title = models.CharField("Заголовок", max_length=32)
    discription = models.CharField("Описание", max_length=64)
    email = models.EmailField("Email", unique=True)
    image = models.ImageField("Фотка",upload_to="images/", default='images/default.png', validators=[
        FileExtensionValidator(allowed_extensions=['png','jpg'])
    ])
    date_of_published = models.DateField("Дата публицации", auto_now_add=True)
    status = models.BooleanField("Статус", default=False)
    categories = models.ManyToManyField('Category', blank=True, related_name="ads")
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/ads'
    
class Category(models.Model):
    title = models.CharField("Название", max_length=32)
    
    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Category)
def delete_related_ads(instance, **kwargs):
    ads = instance.ads.all()
    ads.delete()
