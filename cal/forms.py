from django.forms import ModelForm, DateInput
from cal.models import Event
from datetimewidget.widgets import DateTimeWidget

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      #'data_inicio': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'data_inicio': DateTimeWidget(attrs={'type': 'datetime-local'}, usel10n = True, bootstrap_version=4),
      #'data_fim': DateInput(attrs={'id':'datepicker'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    #self.fields['data_inicio'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['data_fim'].input_formats = ('%Y-%m-%dT%H:%M',)
