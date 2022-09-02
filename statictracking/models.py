from pyexpat import model
from django.db import models

# Create your models here.
class Username(models.Model):
    username = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username}"

class Property(models.Model):
    property_content = models.CharField(max_length=100)
    user = models.ManyToManyField( Username , "user_property" )

    def __str__(self):
        return f"{self.property_content}"

class Game(models.Model):
    game_user = models.ForeignKey( Username , on_delete=models.CASCADE , related_name="games" )
    game_res = models.BooleanField()
    game_properties = models.ManyToManyField( Property , related_name="games" , blank=True )
    cs = models.IntegerField()
    time = models.IntegerField()
    death = models.IntegerField()

    def __str__(self):
        return f"""User_name: {self.game_user} , res : {self.game_res} ,
                properties : { self.game_properties.all() } , 
                cs : {self.cs} , time : {self.time} , death : {self.death} """
