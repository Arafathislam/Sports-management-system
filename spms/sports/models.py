from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Priliminary(models.Model):
  teamname = models.CharField(max_length=100)
  score = models.CharField(max_length=25)
  teamname2 = models.CharField(max_length=100)

  
def __str__(self):
    return self.teamname

  

class SemiFinal(models.Model):
    
  teamname = models.CharField(max_length=100)
  score = models.CharField(max_length=25)
  teamname3 = models.CharField(max_length=100)
  

  
def __str__(self):
    return self.teamname

  

class Final(models.Model):
    
  teamname = models.CharField(max_length=100)
  score = models.CharField(max_length=25)
  teamname4 = models.CharField(max_length=100)
  


def __str__(self):
    return self.teamname


class Entry(models.Model) :
     final = models.ForeignKey(Final,on_delete=models.CASCADE)
     
     headline = models.CharField(max_length=255)
     body_text = models.TextField()
     priliminary = models.ManyToManyField(Priliminary)
     semifinal = models.ManyToManyField(SemiFinal)

     def __str__(self):
         return self.headline

class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)
    height=models.DecimalField(max_length=200,null=True)
    wight=models.DecimalField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    nationality=models.CharField(max_length=200,null=True)
    bio=models.TextField(null=True)

    avatar=models.ImageField(null=True,default="avatar.svg")
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
  
class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
 


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]