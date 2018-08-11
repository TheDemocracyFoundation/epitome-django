#from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class VoteMain(models.Model):
    username = models.CharField(max_length=200)
    area = models.IntegerField(default=0)
    vote_proxy = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        
class VoteResult(models.Model):
    vote_main = models.OneToOneField(VoteMain, on_delete=models.DO_NOTHING)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.votes
        

class VoteTexts(models.Model):
    vote_m = models.OneToOneField(VoteMain, on_delete=models.DO_NOTHING)
    vote_name = models.CharField(max_length=200)
    vote_description = models.CharField
    def __str__(self):
        return self.vote_name
