from django.db import models

# first class
class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    tName = models.CharField(max_length=16, null=False, blank=False)
    profession = models.CharField(max_length=16)

    def __str__(self):
        return self.tName

# second class
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    sName = models.CharField(max_length=16, null=False, blank=False)
    age = models.IntegerField(default=0,null=True, blank=True)
    teacherName = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=True, blank=True)
   
    def __str__(self):
        return self.sName

# theird class
class Coordinators(models.Model):
    id = models.BigAutoField(primary_key=True)
    cName = models.CharField(max_length=16, null=False, blank=False)
    workPlace = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.cName