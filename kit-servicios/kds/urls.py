from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import IndexView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from panel_control.views import PcList,ServiceConfigResource, ServiceStatus, ServiceKeyResource, ServiceRecipeResource
from kds_client.views import HardwareInformation
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^ServiceConfigResource/$', ServiceConfigResource.as_view()),
	url(r'^ServiceStatus/$', ServiceStatus.as_view()),
	url(r'^pclist/$', PcList.as_view()),
	url(r'^hdInfo/$', HardwareInformation.as_view()),
	url(r'^ServiceKeyResource/$', ServiceKeyResource.as_view()),
	url(r'^ServiceRecipeResource/$', ServiceRecipeResource.as_view()),
	url('^.*$', IndexView.as_view(), name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns) + staticfiles_urlpatterns()
