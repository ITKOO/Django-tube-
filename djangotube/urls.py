# djangotube/urls/py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^video/', include(('video.urls', 'video'), namespace='video')),
]
