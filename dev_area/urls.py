from django.conf.urls import url
from .views import staging_area, dev_area

urlpatterns = [
    url(r'^staging/$', staging_area),
    url(r'^ticket/(?P<id>\d+)/$', dev_area),
    ]