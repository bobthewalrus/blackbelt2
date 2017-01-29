from django.conf.urls import url
from views import index, loginvalidate, registervalidate, success, logout, addappt,editappt,submitedit, deleteappt
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^loginvalidate$', loginvalidate, name='loginvalidate'),
    url(r'^registervalidate$', registervalidate, name='registervalidate'),
    url(r'^success$', success, name='success'),
    url(r'^logout$', logout, name='logout'),
    url(r'^addappt$', addappt, name='addappt'),
    url(r'^editappt/(?P<id>\d+)', editappt, name='editappt'),
    url(r'^submitedit/(?P<id>\d+)', submitedit, name='submitedit'),
    url(r'^deleteappt/(?P<id>\d+)', deleteappt, name='deleteappt')
]
