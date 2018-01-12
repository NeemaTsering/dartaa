from django.db import models
from django.utils import timezone
# Create your models here.

class News(models.Model):
	author=models.CharField(max_length=100)
	published_date=models.DateTimeField(default=timezone.now, null=True)
	title=models.CharField(max_length=100)
	text=models.TextField()

	def __str__(self):
		return self.title