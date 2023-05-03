from django.db import models


# Create your models here.
class Phishtank(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Items(models.Model):
    Phishtank = models.ForeignKey(Phishtank, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BinaryField()

    def __str__(self):
        return self.text
