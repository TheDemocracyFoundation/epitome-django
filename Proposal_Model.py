from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class Proposals(models.Model):
	P_CODE = models.CharField(max_length=200)                           #the code of the proposal
	P_TITLE = models.CharField(max_length=100)                          #the title of the proposal
	P_BODY = models.CharField()                                         #the body (main text) of the proposal
	P_CREATION = models.DateTimeField(default = timezone.now())         #the creation date and time of the proposal
	P_STARTDT = models.DateTimeField()                                  #the starting date and time of the proposal
	P_ENDDT = models.DateTimeField()                                    #the ending date and time of the proposal
	P_DURATION = models.IntegerField(default=0)                         #the duration of the proposal
	P_CODE2 = models.CharField(max_length=200)                          #the code2 of the proposal (protocol number, approval number)
	USER_CREATORID = models.ForeignKey(User, on_delete=models.CASCADE)  #the user (admin) who created the proposal
	UGRP_GROUPID = models.ForeignKey(UserGroup, on_delete=models.CASCADE)#the group of the user that created the proposal
	PCAT_CAT = models.ForeignKey(Proposal_Attr)                         #the category of the proposal
	PCHOICE_CHOICE = models.ForeignKey(Proposal_Attr)                   #the voting choices of the proposal
	def __unicode__(self): 
		return "%s %s %s %s %s" % (self.P_TITLE, self.P_BODY, self.P_STARTDT, self.P_ENDDT, self.P_DURATION)
	

class ProposalCat(models.Model):
	PCAT_CAT = models.CharField(max_length=100)                         #the category of the proposal
	def __unicode__(self):
		return self.PCAT_CAT


class ProposalChoice(models.Model):
	PCHOICE_CHOICE = models.IntegerField(default=0)                     #the voting choices of the proposal
	def __unicode__(self):
		return PCHOICE_CHOICE
