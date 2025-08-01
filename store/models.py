#from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # needs Pillow
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name