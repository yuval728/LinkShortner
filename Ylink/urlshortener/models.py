from django.db import models
from .utils import create_shortened_url

# Create your models here.

class Links(models.Model):
    link = models.URLField()
    short = models.CharField(max_length=100, unique=True, blank=True, null=True)
    visits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.link} - {self.short} - {self.visits} - {self.created_at}'
    
    def save(self, *args, **kwargs):
        
        if self.short is None or self.short == '':
            self.short = create_shortened_url(self)
            
        super().save(*args, **kwargs)
        
    