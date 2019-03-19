from django.conf.urls import url
from .views import view_ticket, new_ticket, view_comments, new_comment, up_vote


urlpatterns = [
    url(r'^view/(?P<id>\d+)/$', view_ticket, name="view_ticket"),
    url(r'^new/(?P<type>[\w.@+-]+)/', new_ticket, name="new_ticket"),
    url(r'^view/(?P<id>\d+)/comments/', view_comments, name="view_comments"),
    url(r'^view/(?P<id>\d+)/new_comment/', new_comment, name="new_comment"),
    url(r'^upvote/(?P<id>\d+)/', up_vote, name="up_vote"),
    ]