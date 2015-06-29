from django.db import models




class Story(models.Model):
	caption = models.CharField(max_length=200)
	#comments = models.OneToManyField()
	description = models.CharField(max_length=100)
	checked = models.BooleanField(default=False)
	
class Comments(models.Model):
	text = models.CharField(max_length=500)
	