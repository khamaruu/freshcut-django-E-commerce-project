from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from adminpage.models import Product
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')
        
    @property
    def subtotal(self):
        return (self.product.price) * self.quantity
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username    