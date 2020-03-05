from django.db import models


class Resume(models.Model):
    CV = models.FileField(verbose_name="Resume", upload_to=None, max_length=400)


class contact(models.Model):
    name = models.CharField(verbose_name="Name",max_length=150)
    Email= models.EmailField(verbose_name="Email Address", max_length=254)
    Mobile = models.IntegerField(verbose_name="Mobile Number")
    Msg = models.TextField(verbose_name="Message",max_length=400)
