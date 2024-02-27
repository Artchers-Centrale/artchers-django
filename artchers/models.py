from django.db import models

# Create your models here.

class district(models.Model):
    nom = models.CharField(max_length=200)
    image = models.FileField(upload_to="images")
    image_el = models.FileField(upload_to="images")
    is_eliminated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nom


class vote(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    vote = models.ForeignKey(district, on_delete=models.CASCADE)
    isConfirmed = models.BooleanField(default=False)
    key = models.CharField(max_length=200, default='Null')

    def __str__(self) -> str:
        return str(self.prenom) + " " + str(self.nom)
    

class OneTimeLinkModel(models.Model):
    one_time_code = models.CharField(max_length=20)