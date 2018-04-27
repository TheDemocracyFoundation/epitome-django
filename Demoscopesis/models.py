#from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class PollCat(models.Model):
	PCAT_CAT = models.CharField("Poll category", max_length=100)                                         # the category of the poll
	def __str__(self):
		return self.PCAT_CAT
	class Meta:
		verbose_name = 'Poll category'
		verbose_name_plural = 'Poll categories'


class Poll(models.Model):
	PL_CODE = models.CharField("Code", max_length=200)                                                   # the code of the poll
	PL_TITLE = models.CharField("Title", max_length=200)                                                 # the title of the poll
	PL_SHRBODY = models.CharField("Short body", max_length=300)                                          # the short body of the poll
	PL_BODY = models.CharField("Body", max_length=1000)                                                  # the body (main text) of the poll
	PL_CREATION = models.DateTimeField("Creation date", default = timezone.now)                          # the creation date and time of the poll
	PL_STARTDT = models.DateTimeField("Starting date")                                                   # the starting date and time of the poll
	PL_ENDDT = models.DateTimeField("Ending date")                                                       # the ending date and time of the poll
	PL_DURATION = models.IntegerField("Duration", default=0)                                             # the duration of the poll
	PL_CODE2 = models.CharField("Code 2", max_length=200, blank = True)                                  # the code2 of the poll (protocol number, approval number)
	USER = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")                        # the user (admin) who created the poll
	UGROUP = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="User group")               # the group of the user that created the poll
	POLLCAT = models.ForeignKey(PollCat, on_delete=models.CASCADE, verbose_name="Poll category")         # the category of the poll
	def __str__(self): 
		return "%s %s" % (self.PL_TITLE, self.PL_SHRBODY)


class PollChoice(models.Model):
	POLL = models.ForeignKey(Poll, related_name='PChoice', on_delete=models.CASCADE)                     # key to Polls table
	PC_CHOICE = models.CharField("Choice", max_length=100)                                               # the vote choice
	PC_VOTES = models.IntegerField("Votes", default=0)                                                   # the number of votes
	def __str__(self):
		return self.PC_CHOICE


class Voter(models.Model):
	USER = models.ForeignKey(User, on_delete=models.CASCADE)
	POLL = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Issue(models.Model):
	IS_CODE = models.CharField("Code", max_length=200)                                                   # the code of the issue
	IS_TITLE = models.CharField("Title", max_length=200)                                                 # the title of the issue
	IS_SHRBODY = models.CharField("Short body", max_length=300)                                          # the short body of the issue
	IS_BODY = models.CharField("body", max_length=1000)                                                  # the body (main text) of the issue
	IS_CREATION = models.DateTimeField("Creation date", default = timezone.now)                          # the creation date and time of the issue
	IS_CODE2 = models.CharField("Code 2", max_length=200, blank = True)                                  # the code2 of the issue (protocol number, approval number)
	USER = models.ForeignKey(User, on_delete=models.CASCADE)                                             # the user (admin) who created the issue
	UGROUP = models.ForeignKey(Group, on_delete=models.CASCADE)                                          # the group of the user that created the issue
	def __str__(self): 
		return "%s %s" % (self.IS_TITLE, self.IS_SHRBODY)


class Evidence(models.Model):
	EV_FLD1 = models.CharField(max_length=1000)                                                          # What has happened?
	EV_FLD2 = models.CharField(max_length=1000)                                                          # Why is it important?
	EV_FLD3 = models.CharField(max_length=1000)                                                          # Who has been affected?
	EV_FLD4 = models.CharField(max_length=1000)                                                          # How and why did it happen?
	EV_FLD5 = models.CharField(max_length=1000)                                                          # Where did it occur?
	EV_FLD6 = models.CharField(max_length=1000)                                                          # When did it occur?
	EV_FLD7 = models.CharField(max_length=1000)                                                          # How much is the cost?
	EV_FLD8 = models.CharField(max_length=1000)                                                          # How long did it last?
	ISSUE = models.ForeignKey(Issue, on_delete=models.CASCADE)                                           # key to Issues table
