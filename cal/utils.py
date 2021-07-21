import locale
from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, day=None):
		# Eduardo Ceratti - force local usage
		locale.setlocale(locale.LC_ALL,'pt_BR')
		
		self.year = year
		self.month = month
		self.day = day
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, week, year, month, events):
		events_per_day = events.filter(data_inicio__day=day)
		now_date = date.today().strftime("%Y-%m-%d")
		d = ''

		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'		
		
		# Eduardo Ceratti
		if day != 0:
			if (date(year, month, day).isoformat()) == now_date:
				return f"<td style='background-color:#C1EAEC'><span class='date'>{day}</span><ul> {d} </ul></td>"
			else:	
				return f"<td><span class='date'><a href='/detail/view/{year}-{month}-{day}/'>{day}</a></span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, year, month, events):
		week = ''

		for d, weekday in theweek:
			week += self.formatday(d, weekday, year, month, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(data_inicio__year=self.year, data_inicio__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, self.year, self.month, events)}\n'
		return cal

	def formatdaydetail(self):

		events = Event.objects.filter(data_inicio__year=self.year, data_inicio__month=self.month, data_inicio__day=self.day)
		print(events)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'

		return cal

