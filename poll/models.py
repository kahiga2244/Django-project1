from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    email = models.EmailField()


    def __str__(self):
        return self.id
    class Meta:
        ordering = ['id']
    
    def save_user(self):
        self.save()

class Poll(models.Model):
    president = models.CharField(max_length=30)
    political_party = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)
    poll_number = models.IntegerField(default=0)

   

