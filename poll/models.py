from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    email = models.EmailField()


    def __str__(self):
        return self.user_id
    class Meta:
        ordering = ['user_id']
    
    def save_user(self):
        self.save()
    
    def delete_user(self):
        self.delete()


class Poll(models.Model):
    president = models.CharField(max_length=30)
    # user = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE,
    #     related_name="Polls",
    #     related_query_name = "poll"
    # )
    political_party = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)
    poll_number = models.IntegerField(default=0)

    def __str__(self):
        return self.president
    class Meta:
        ordering = ['president']
    
    def save_user(self):
        self.save()
    def delete_user(self):
        self.delete()


   

