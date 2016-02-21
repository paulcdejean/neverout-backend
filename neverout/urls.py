from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import backend.views

urlpatterns = [
    url(r'^$', backend.views.index, name='index'),
    url(r'^db', backend.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
