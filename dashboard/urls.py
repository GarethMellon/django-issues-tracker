from django.conf.urls import url
from .views import dashboard_page

urlpatterns =[
    url(r'^$/', dashboard_page, name="dashboard"),
    ]