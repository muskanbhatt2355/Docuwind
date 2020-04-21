from django.db import models

# Create your models here.
class Student3(models.Model):
	firstname = models.CharField(max_length=100,unique=False)
	start_time = models.CharField(max_length=100,unique=False)
	phone_no = models.CharField(max_length=10,unique=False)
	res_id = models.IntegerField(unique=False)
	
