from django.contrib import admin

from Eisegesis.models import Proposals
from Eisegesis.models import ProposalCat
from Eisegesis.models import ProposalChoice


class ProposalInline(admin.StackedInline):
	model = PollChoice
	extra = 3

    
class EisegesisAdmin(admin.ModelAdmin):
	list_display = ('P_TITLE', 'P_SHRBODY', 'P_CREATION', 'USER_CREATORID')
	fieldsets = [
		(None,               {'fields': ['P_TITLE', 'P_SHRBODY', 'P_BODY']}),
		('Date information', {'fields': ['P_CREATION', 'P_STARTDT', 'P_ENDDT', 'P_DURATION']}),
		('Code information', {'fields': ['P_CODE', 'P_CODE2']}),
		('User and Category information', {'fields': ['USER_CREATORID', 'UGRP_GROUPID', 'PCAT_CAT']}),
	]
	inlines = [PollInline]


admin.site.register(Polls, EisegesisAdmin)
admin.site.register(PollCat)
admin.site.register(PollChoice)
