from django.conf.urls import url
from .views import view_ticket, new_ticket, view_comments, new_comment


urlpatterns = [
    url(r'^view/(?P<id>\d+)/$', view_ticket, name="view_ticket"),
    url(r'^new/', new_ticket, name="new_ticket"),
    url(r'^view/(?P<id>\d+)/comments/', view_comments, name="view_comments"),
    url(r'^view/(?P<id>\d+)/new_comment/', new_comment, name="new_comment"),
    ]