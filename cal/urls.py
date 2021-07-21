from django.conf.urls import url
from django.urls import path
#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'cal'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),

   

    # Eduardo Ceratti
    #url(r'^detail/view/$', views.day_detail, name='detail_view'),
    path('detail/view/<day>/', views.day_detail, name='detail_view'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/calendar'), name='logout'),



]
