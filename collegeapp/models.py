from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=70)
    Course_Fees=models.IntegerField()
        
class StudentModel(models.Model):
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Stud_Name=models.CharField(max_length=100)
    Stud_Address=models.CharField(max_length=200)
    Stud_Age=models.IntegerField() 

class Usermember(models.Model):
    Teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Tr_Address=models.CharField(max_length=200)
    Tr_Age=models.IntegerField()
    Tr_gender=models.CharField(max_length=10)
    Tr_image=models.ImageField(upload_to='image/')
