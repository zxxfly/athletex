from django.conf.urls import patterns, include, url
from sports import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'L01_BootStrapDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)


urlpatterns += staticfiles_urlpatterns()
