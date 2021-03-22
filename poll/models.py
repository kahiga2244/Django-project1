from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    Ruto_Samoei = models.CharField(max_length=30)
    Raila_Amolo = models.CharField(max_length=30)
    Mudavadi_Musalia = models.CharField(max_length=30)
    Gideon_Moi = models.CharField(max_length=30)
    Kivutha_Kibwana = models.CharField(max_length=30)
    Kituyi_Mukhisa = models.CharField(max_length=30)

    Ruto_Samoei_count = models.IntegerField(default=0)
    Raila_Amolo_count = models.IntegerField(default=0)
    Mudavadi_Musalia_count = models.IntegerField(default=0)
    Gideon_Moi_count = models.IntegerField(default=0)
    Kivutha_Kibwana_count = models.IntegerField(default=0)
    Kituyi_Mukhisa_count = models.IntegerField(default=0)

