from django.conf.urls import url
from .views import staging_area, staging_ticket, dev_area, dev_ticket, staging_accept, staging_reject

urlpatterns = [
    url(r'^staging-board/$', staging_area, name="staging"),
    url(r'^staging-ticket/(?P<id>\d+)/$', staging_ticket, name="staging_ticket"),
    url(r'^staging-accept/(?P<id>\d+)/$', staging_accept, name="staging_accept"),
    url(r'^staging-reject/(?P<id>\d+)/$', staging_reject, name="staging_reject"),
    url(r'^dev-board/$', dev_area, name="dev_area"),
    url(r'^dev-ticket/(?P<id>\d+)/$', dev_ticket, name="dev_ticket"),
    ]