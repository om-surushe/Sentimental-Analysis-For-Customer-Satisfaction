from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=300,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    role = models.CharField(max_length=300,null=False,blank=False)
    q1 = models.TextField(null=False,blank=False)
    q1s = models.CharField(max_length=10,null=False,blank=False)
    q2 = models.TextField(null=False,blank=False)
    q2s = models.CharField(max_length=10,null=False,blank=False)
    q3 = models.TextField(null=False,blank=False)
    q3s = models.CharField(max_length=10,null=False,blank=False)
    q4 = models.TextField(null=False,blank=False)
    q4s = models.CharField(max_length=10,null=False,blank=False)

    def _str_(self):
        return str(self.name)