from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, blank=False
    )
    address = models.CharField(max_length=100, default="")
    street = models.CharField(max_length=100, default="")
    pincode = models.CharField(max_length=10, default="")
    image = models.ImageField(upload_to="app1/images", default="")

    def __str__(self):
        return self.user.username
