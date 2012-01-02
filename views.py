from andrewgardner.Calendar.models import Calendar
from django.http import Http404

def get_calendar_month(request, year, month):
	get = request.GET
	if request.is_ajax():
		calendar_id = get['calendar_id']
	else:
		raise Http404