from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return self.name