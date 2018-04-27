from django.contrib import admin

from Demoscopesis.models import Poll
from Demoscopesis.models import PollCat
from Demoscopesis.models import PollChoice


class PollInline(admin.StackedInline):
	model = PollChoice
	extra = 3

    
class DemoscopesisAdmin(admin.ModelAdmin):
	list_display = ('PL_TITLE', 'PL_SHRBODY', 'PL_CREATION', 'USER')
	fieldsets = [
		(None,               {'fields': ['PL_TITLE', 'PL_SHRBODY', 'PL_BODY']}),
		('Date information', {'fields': ['PL_CREATION', 'PL_STARTDT', 'PL_ENDDT', 'PL_DURATION']}),
		('Code information', {'fields': ['PL_CODE', 'PL_CODE2']}),
		('User and Category information', {'fields': ['USER', 'UGROUP', 'POLLCAT']}),
	]
	inlines = [PollInline]


admin.site.register(Poll, DemoscopesisAdmin)
admin.site.register(PollCat)
admin.site.register(PollChoice)
