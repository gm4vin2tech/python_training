from django.db import models

# Create your models here.
class Teacher(models.Model):
	name = models.CharField(max_length=80)
	age = models.IntegerField()

class Teacher1(models.Model):
	name = models.CharField(max_length=80)
	age = models.IntegerField()	

class Teacher2(models.Model):
	name = models.CharField(max_length=80)
	age = models.IntegerField()

class Destination(models.Model):
	name = models.CharField(max_length=100)
	# img = models.ImageField(upload_to='pics') #"python -m pip install Pillow" for accessing Image field
	desc = models.TextField()
	offer = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Destination1(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	offer = models.BooleanField(default=False)

	def __str__(self):
		return self.name