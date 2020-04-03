from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):

        return self.description[:200]
