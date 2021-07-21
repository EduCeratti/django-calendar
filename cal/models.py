from django.db import models
from django.urls import reverse

class Event(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        
        # Eduardo Ceratti - Date with Hour
        init_date = self.data_inicio.strftime("%H:%M")
        return f'<a href="{url}"> {init_date} - {self.titulo} </a>'
