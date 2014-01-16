from django.conf.urls import patterns, url
from edittags import views

urlpatterns = patterns('', 
                       url(r'^$', views.edittags, name='edittags')
)
