from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Modir(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    codemeli = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    def __str__ (self):
        return self.firstname


class Charity(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=60)
    sabt_number = models.CharField(max_length=30)
    description = models.TextField()
    web = models.URLField()
    photo = models.ImageField(blank=True)
    photo_sanad = models.ImageField(default='default.png')
    modir = models.OneToOneField(User , on_delete=models.CASCADE )
    accept = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Dastebanamdy_ch(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Dastebanamdy_LD(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TypeCampain(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class ProjectType(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    #projectType = models.ForeignKey(ProjectType, on_delete = models.CASCADE)

    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length=50)
    cost = models.FloatField()
    description = models.TextField()
    modir= models.ForeignKey(User, on_delete=models.CASCADE)
    projectType = models.ForeignKey(ProjectType, on_delete = models.CASCADE , default=1 )
    cration_date = models.DateField(auto_now_add=True)
    dastebandy_G=models.ForeignKey(Dastebanamdy_ch , null = True , on_delete=models.CASCADE , default="")
    dastebanamdy_LD = models.ForeignKey(Dastebanamdy_LD , null = True , on_delete=models.CASCADE , default="")
    campain_typ = models.ForeignKey(TypeCampain , null = True , on_delete=models.CASCADE , default="")
    charity = models.ForeignKey(Charity , on_delete=models.CASCADE , default="" )
    user= models.ManyToManyField(User,related_name='userPaid', through='participateProject')

    def __str__(self):
        return self.title


class participateProject(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    paid = models.FloatField()
    seSote = models.BooleanField(default=False)
    paidDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project.name
