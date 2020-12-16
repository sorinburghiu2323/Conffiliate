from django.db import models

# Create your models here.


class PreRegisterUser(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
