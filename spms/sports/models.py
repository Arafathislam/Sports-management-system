from django.db import models


Create your models here.
class Registeration(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    height=models.DecimalField(max_digits=7,decimal_places=2)
    gender=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)
    age=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    dateofbirth=models.CharField(max_length=200,null=True)
    nationality=models.CharField(max_length=200,null=True)
    number=name=models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)


class Contact(models.Model):
     fname=models.CharField(max_length=200,null=True)
     lname=models.CharField(max_length=200,null=True)
     email=models.CharField(max_length=200,null=True)
     number=name=models.CharField(max_length=200,null=True)
     msg=models.CharField(max_length=200,null=True)

class Members(models.Model) :
    teamname = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    date = models.DateField()



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
     
