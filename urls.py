from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from calendar.models import Calendar
#Calendar related url patters
try:
	calendar = Calendar.objects.get(id=1)
except:
	calendar = Calendar.objects.create(name='home_calendar')

urlpatterns = patterns('calendar.views',
	(r'^$',                                  direct_to_template, {
		'template':'object_view/calendar_mini.html',
		'extra_context' : {
			'calendar' : calendar.month_as_table(2011,12)}
		}),
)