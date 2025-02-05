from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator

# Create your models here.


class Ad(models.Model):
    title = models.CharField("Заголовок обьявления", max_length=32)
    discription = models.CharField("Описание обьявления", max_length=64)
    img = models.ImageField(upload_to='images/', default='images/default.png', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg'])
    ])
    email = models.EmailField("Адрес электронной почты автора"  , unique=True)
    date_of_published = models.DateField("Дата публикации",auto_now_add=True)
    status = models.BooleanField("Статус",default=False)
    
    categories = models.ManyToManyField('Category', blank=True, related_name="ads")
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"
        
        
    def get_absolute_url(self):
        return '/ads'
    
class Category(models.Model):
    title = models.CharField("Заголовок категории", max_length=32)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


@receiver(pre_delete, sender=Category)
def delete_related_ads(instance, **kwargs):
    ads = instance.ads.all()
    ads.delete()
