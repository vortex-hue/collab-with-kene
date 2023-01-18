from django.db import models

class Home(models.Model):
    pass

class About(models.Model):
    about_text = models.TextField()
    image = models.ImageField()

class Affiliate(models.Model):
    paragraph1 = models.TextField()
    emphasized = models.TextField()
    paragraph2 = models.TextField()