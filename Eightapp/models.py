from django.db import models

# Create your models here.

class Game(models.Model):
    Game_Name=models.CharField(max_length=50)

class Player(models.Model):
    Player_Name = models.CharField(max_length=50)
    Player_Age = models.IntegerField()
    Player_Phno = models.BigIntegerField()
    Player_Game_Type = models.ForeignKey(Game,on_delete=models.CASCADE)



