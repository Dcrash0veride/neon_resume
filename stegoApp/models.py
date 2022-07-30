from django.db import models

# Create your models here.
class stegoImagesModel(models.Model):
    uploadedImage = models.ImageField(upload_to='stego/upload/')
    secretMessage = models.CharField(max_length=200)
    messageHash = models.CharField(max_length=64, default='00000000')
    comboHash = models.CharField(max_length=64, default='00000000', primary_key=True)
    webLink = models.URLField(blank=True)

    def __str__(self):
        return self.comboHash

class stegoDecodeModel(models.Model):
    s_message = models.CharField(max_length=200)
    enc_img_hash = models.CharField(max_length=64)
    double_hash = models.CharField(max_length=64, primary_key=True)


    def __str__(self):
        return self.double_hash
