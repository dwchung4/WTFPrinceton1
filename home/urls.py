from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^(?P<sort>[a-zA-Z]*)$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/(?P<next_page>[0-9a-z_/]*)$', 'cas.views.login', name='login'),
	url(r'^logout/$', 'cas.views.logout', name='logout'),
	url(r'^create_petition/$', views.create_petition, name='create_petition'),
	url(r'^add_comment/(?P<id>[0-9a-z]+)/$', views.add_comment, name='add_comment'),
	url(r'^my_petitions/(?P<netid>[a-z]+[0-9a-z]*)/$', views.my_petitions, name='my_petitions'),
	url(r'^delete_petition/(?P<petitionid>[0-9]+)$', views.delete_petition, name='delete_petition'),
	url(r'^vote/(?P<petitionid>[0-9]+)/(?P<netid>[0-9a-z]*)$', views.vote, name='vote'),
	url(r'^howtouse/$', views.howtouse, name='howtouse'),
]