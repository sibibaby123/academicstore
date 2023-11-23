from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='department',unique=True)
    email=models.EmailField()

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)
    
class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)
    department=models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE
    )    
class Purpose(models.Model):
    name=models.CharField(max_length=20,null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    
class UserExtra(models.Model):
    user = models.ForeignKey(to=User, on_delete = models.CASCADE)
    age=models.IntegerField()
    dateofbirth=models.DateField()
    gender=models.BooleanField(default=True)
    address=models.TextField(max_length=250)
    phonenumber=models.CharField(max_length=20,unique=True)
    course=models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,null=True,blank=True,default=None
    )
    purpose=models.CharField(max_length=20, default="", null=True, blank=True)
    exampaper=models.CharField(max_length=20, default="", null=True, blank=True)
    pen=models.CharField(max_length=20, default="", null=True, blank=True)
    material=models.CharField(max_length=20, default="", null=True, blank=True)
    books=models.CharField(max_length=20, default="", null=True, blank=True)
    newspaper=models.CharField(max_length=20, default="", null=True, blank=True)

