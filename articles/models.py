from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class SportsMen(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    preview = models.CharField(max_length=630, null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    
    def __str__(self):
        return self.name