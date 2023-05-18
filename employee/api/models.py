from django.db import models




class Employes(models.Model):
    name=models.CharField(max_length=10)
    age=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    salary=models.PositiveBigIntegerField()


    def __str__(self): 
        return self.name()


