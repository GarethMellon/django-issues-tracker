"""issues_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import dashboard_page, charge

from accounts import urls as accounts_urls
from tickets import urls as tickets_urls
from dev_area import urls as dev_area_urls
from contact_us import urls as contact_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dashboard_page, name="dashboard_page"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^tickets/', include(tickets_urls)),
    url(r'^development/', include(dev_area_urls)),
    url('charge/(?P<id>\d+)/(?P<up_vote_flag>[\w.@+-]+)', charge, name='charge'),
    url(r'^contact/', include(contact_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)