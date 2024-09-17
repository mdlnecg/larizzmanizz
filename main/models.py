<<<<<<< HEAD
import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.CharField(max_length=5, default='⭐⭐⭐⭐')
=======
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Field untuk URL gambar produk
>>>>>>> 65c6553ca8fcd7cdd99e145cf0c3d98d1e605d7b

    def __str__(self):
        return self.name
