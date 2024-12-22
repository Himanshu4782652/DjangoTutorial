from django.db import models

# Create your models here.

#Model created
class Teacher(models.Model):
 FirstName=models.CharField(max_length=50)
 LastName=models.CharField(max_length=50)
 Email=models.EmailField(max_length=50)
 Contact=models.CharField(max_length=50)
 
 #this function is used for converting object into strings
 def __str__(self) -> str:
  return self.FirstName