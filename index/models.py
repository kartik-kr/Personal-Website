from django.db import models

class ContactMe(models.Model):
        name = models.CharField(max_length = 128)
        mail = models.CharField(max_length =500)
        mobile = models.CharField(max_length = 15)
        message = models.CharField(max_length = 2000)
        def __str__(self):
                return self.name + " " + self.message
