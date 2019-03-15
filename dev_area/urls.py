from django.conf.urls import url
from .views import staging_area, staging_ticket

urlpatterns = [
    url(r'^staging/$', staging_area),
    url(r'^staging/ticket/(?P<id>\d+)/$', staging_ticket),
    ]