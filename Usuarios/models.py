from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class Usuario(AbstractUser):
    uuid = models.UUIDField(auto_created=True,default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID',editable=False)
    telefono = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
