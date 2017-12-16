from django.contrib import admin

from Eisegesis.models import Poll
from Eisegesis.models import PollCat
from Eisegesis.models import PollChoice


class PollInline(admin.StackedInline):
	model = PollChoice
	extra = 3

    
class EisegesisAdmin(admin.ModelAdmin):
	list_display = ('PL_TITLE', 'PL_SHRBODY', 'PL_CREATION', 'USER')
	fieldsets = [
		(None,               {'fields': ['PL_TITLE', 'PL_SHRBODY', 'PL_BODY']}),
		('Date information', {'fields': ['PL_CREATION', 'PL_STARTDT', 'PL_ENDDT', 'PL_DURATION']}),
		('Code information', {'fields': ['PL_CODE', 'PL_CODE2']}),
		('User and Category information', {'fields': ['USER', 'UGROUP', 'POLLCAT']}),
	]
	inlines = [PollInline]


admin.site.register(Poll, EisegesisAdmin)
admin.site.register(PollCat)
admin.site.register(PollChoice)
