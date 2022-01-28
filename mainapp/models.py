from django.db import models

class Question(models.Model):

	question_text = models.CharField(max_length=500)
	answer1 = models.CharField(max_length=200)
	answer2 = models.CharField(max_length=200)
	answer3 = models.CharField(max_length=200)
	answer4 = models.CharField(max_length=200)

	def __str__(self):
		return self.question_text