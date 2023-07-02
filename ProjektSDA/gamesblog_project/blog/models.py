from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    data = models.DateField()
    image = models.ImageField(upload_to="images", blank=True)

    #dunder metho = double underscore method
    def __str__(self):
        return f'{self.data} | {self.title}'