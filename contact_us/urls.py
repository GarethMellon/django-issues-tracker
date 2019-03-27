from django.conf.urls import url
from .views import contact_us, contact_success, complaints

urlpatterns = [
    url(r'^$', contact_us, name="contact_us"),
    url(r'^success$', contact_success, name="contact_success"),
    url(r'^complaints', complaints, name="complaints"),
    ]