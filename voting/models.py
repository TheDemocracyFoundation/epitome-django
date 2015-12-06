import datetime

from django.db import models
from django.utils import timezone


class Vote_main(models.Model):
    username = models.CharField(max_length=200)
    area = models.IntegerField(default=0)
    voteProxy = models.IntegerField(default=0)
    pubDate = models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

		
class Vote_result(models.Model):
    voteMain = models.OneToOneField(Vote_main)
    votes = models.IntegerField(default=0)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.votes
        

class Vote_texts(models.Model):
    voteM = models.OneToOneField(Vote_main)
    voteName = models.CharField(max_length=200)
    voteDescription = models.CharField
    def __unicode__(self):              # __unicode__ on Python 2
        return self.vote_name


class UserExtra(models.Model):
	user = models.OneToOneField(User)
	areaOfResidence = models.CharField(max_length=100)
	userID = models.IntegerField
	def __unicode__(self):
        return self.user.username
	
