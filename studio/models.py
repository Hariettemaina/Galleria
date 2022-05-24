from django.db import models
import datetime as dt

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_photographer(self):
        self.save()
        
   
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
        
class Images(models.Model):
    title = models.CharField(max_length =60)
    photographer = models.ForeignKey(Photographer,on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/', null=True)
    
    
    
    @classmethod
    def search_by_title(cls,search_term):
        studio = cls.objects.filter(title__icontains=search_term)
        return studio



   
    
    
