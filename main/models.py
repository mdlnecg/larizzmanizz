from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Field untuk URL gambar produk

    def __str__(self):
        return self.name
