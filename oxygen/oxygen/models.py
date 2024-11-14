from django.db import models
class gymfield(models.Model):
	gymchoachname=models.CharField(max_length=50)
	datetime=models.DateTimeField()
	Location=models.CharField(max_length=40)
	feesturcture=models.CharField(max_length=40)
