from django.db import models

# Create your models here.

class CFgmail(models.Model):
    fname = models.CharField(max_length=64)
    email_address = models.EmailField(max_length=254)
    content = models.CharField(max_length=500)
    # utilizing more combo hash to prevent duplicate info in db
    content_address_hash = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return self.content_address_hash