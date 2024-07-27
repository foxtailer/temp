from django.db import models
import datetime 
from django.utils import timezone

# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField("date published")

  def __str__(self): 
    return self.question_text
  
  def was_published_recently(self): 
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model): 
  question = models.ForeignKey(Question, on_delete=models.CASCADE) 
  choice_text = models.CharField(max_length=200) 
  votes = models.IntegerField(default=0)

  def __str__(self): 
    return self.choice_text


class Rate(models.Model):
    rate_value = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    
    def __str__(self):
        return str(self.rate_value)


class QuestionRate(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
