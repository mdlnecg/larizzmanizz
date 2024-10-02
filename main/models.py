import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField(default=5)
    image_url = models.URLField(default="https://i.pinimg.com/564x/2d/79/f2/2d79f220b35720725ac20410a6b31ac5.jpg")

    def __str__(self):
        return self.name
