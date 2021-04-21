from django.db import models


class Clinic(models.Model):
    Name=models.CharField(max_length=200,unique=True)
    Address=models.CharField(max_length=300)
    Contact=models.CharField(max_length=100)
    Email=models.CharField(max_length=150)
    def __str__(self):
        return self.Name

class Admin(models.Model):
    Name=models.CharField(max_length=200)
    Password=models.CharField(max_length=150)
    BirthDate=models.DateField()
    Address=models.CharField(max_length=300)
    Contact=models.CharField(max_length=100)
    Email = models.CharField(max_length=150)
    Photo = models.CharField(max_length=100)
    PhotoPath = models.CharField(max_length=100)
    Admin_Clinic =models.ForeignKey(Clinic,related_name='admins',on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
class Physiotherapist(models.Model):
    Name =models.CharField(max_length=200)
    Password =models.CharField(max_length=150)
    BirthDate =models.DateField()
    Address =models.CharField(max_length=300)
    Contact =models.CharField(max_length=100)
    Email =models.CharField(max_length=150)
    Photo =models.CharField(max_length=100)
    PhotoPath=models.CharField(max_length=100)
    Clinic_Physio=models.ForeignKey(Clinic,related_name='pysio_therpists',on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
class Patient(models.Model):
    Name=models.CharField(max_length=200)
    Password=models.CharField(max_length=150)
    BirthDate=models.DateField()
    Address=models.CharField(max_length=300)
    Contact=models.CharField(max_length=100)
    Email = models.CharField(max_length=150)
    Photo = models.CharField(max_length=100)
    PhotoPath = models.CharField(max_length=100)
    Gender=models.IntegerField()
    Physio_Patient=models.ForeignKey(Physiotherapist,related_name='patients',on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
class Favorite(models.Model):
    Physio_Favorite=models.ForeignKey(Physiotherapist,related_name='Physio_Fav',on_delete=models.CASCADE)
    Patient_Favorite=models.ForeignKey(Patient,related_name='Patient_Fav',on_delete=models.CASCADE)
class Game(models.Model):
    Name=models.CharField(max_length=80)
    Description=models.CharField(max_length=250)
class Exercise_Plan(models.Model):
    DateOfStart=models.DateField()
    DateOfEnd=models.DateField()
    Duration=models.FloatField()
    RestTime=models.FloatField()
    RepitionNum=models.IntegerField()
    MembersToUse=models.IntegerField()
    Difficulty=models.IntegerField()
    Notes=models.CharField(max_length=500)
    Physio_Exerplan=models.ForeignKey(Physiotherapist,related_name='Physio_Plan',on_delete=models.CASCADE)
    Patient_Exerplan=models.ForeignKey(Patient,related_name='Patient_Plan',on_delete=models.CASCADE)
    Game_Exerplan=models.ForeignKey(Game,related_name='Game_Plan',on_delete=models.CASCADE)
class Session(models.Model):
    DateOfCreation=models.DateTimeField()
    Description=models.CharField(max_length=300)
    Session_Plan=models.ForeignKey(Exercise_Plan,related_name='session_plan',on_delete=models.CASCADE)
class Observations(models.Model):
    DateOfCreation=models.DateTimeField()
    Notes=models.CharField(max_length=300)
    Session_Observation=models.ForeignKey(Session,related_name='session_observ',on_delete=models.CASCADE)
    Patient_Observation=models.ForeignKey(Patient,related_name='patient_observ',on_delete=models.CASCADE)


