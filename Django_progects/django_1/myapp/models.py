import datetime

from django.db import models
from django.utils import timezone


class Questions(models.Model):
    question_text = models.CharField(max_length=300)
    date_public = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_public <= now
    was_published.admin_order_field = 'date_public'
    was_published.boolean = True
    was_published.short_description = "Published ?"


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
