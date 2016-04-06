from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
import django_cas

urlpatterns = [
	url(r'^', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^login/$', 'cas.views.login', name='login'),
	url(r'^logout/$', 'cas.views.logout', name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)