from django.db import models

# Create your models here.
class Data(models.Model):
	name=models.CharField(max_length=120)
	roll_no=models.PositiveIntegerField(default=0)

	def __str__(self):
		return(self.name)