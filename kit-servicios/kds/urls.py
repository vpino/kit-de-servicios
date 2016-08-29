from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import IndexView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from panel_control.views import PcList, ServiceMetadataResource, ServiceConfigResource, ServiceStatus, ServiceKeyResource
from kds_client.views import HardwareInformation
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


"""
router = routers.SimpleRouter()
router.register(r'pclist', PcList, 'PcList')
router.register(r'hdInfo', HardwareInformation, 'hdInfo')
router.register(r'ServiceConfigResource', ServiceConfigResource, 'ServiceConfigResource')
"""

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^api/v1/', include(router.urls)),
	#url(r'^$', homepage, name='index'),
	url(r'^ServiceMetadataResource/(?P<service_name>[a-z]+)$', ServiceMetadataResource.as_view()),
	url(r'^ServiceConfigResource/$', ServiceConfigResource.as_view()),
	url(r'^ServiceStatus/$', ServiceStatus.as_view()),
	url(r'^pclist/$', PcList.as_view()),
	url(r'^hdInfo/$', HardwareInformation.as_view()),
	url(r'^ServiceKeyResource/$', ServiceKeyResource.as_view()),
	url('^.*$', IndexView.as_view(), name='index'),

]

urlpatterns = format_suffix_patterns(urlpatterns) + staticfiles_urlpatterns()
