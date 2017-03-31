from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^([0-9]+)/$',
		views.detail, name = 'detail'),
	url(r'^post_url/$', views.post_photograph, name='post_photograph'),
	url(r'^user/(\w+)/$', views.profile, name = 'profile'),
	url(r'^login/$', views.login_view, name ='login'),
	url(r'^logout/$', views.logout_view, name ='logout'),
	url('^like_photograph/$', views.like_photograph, name='like_photograph')
]



# Sends any url that matches media/ to a built-in Django view called static.serve()
# Necessary when uploading files
if settings.DEBUG: 
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', serve, 
		{'document_root': settings.MEDIA_ROOT,}),
	]