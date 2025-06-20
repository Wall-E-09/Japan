from django.db import models

# Create your models here.
class JapanAlphabet(models.Model):
    title = models.CharField('Title', max_length=50)
    symbols = models.CharField('Symbols', max_length=10)
    full_text = models.TextField('Full text')
    # MySQL specific configurations are handled in settings.py
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Japanese alphabet'
        verbose_name_plural = 'Japanese alphabets'