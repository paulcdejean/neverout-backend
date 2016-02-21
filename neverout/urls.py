from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import backend.views

urlpatterns = [
    url(r"^add_point/([-+]?[0-9]*\.?[0-9]+)$", backend.views.add_point, name="add_point"),
    url(r"set_empty/([-+]?[0-9]*\.?[0-9]+)$", backend.views.set_empty, name="set_empty"),
    url(r"set_full/([-+]?[0-9]*\.?[0-9]+)$", backend.views.set_full, name="set_full"),
    url(r'^$', backend.views.index, name='index'),
    url(r'^name$', backend.views.name, name='name'),
    url(r'^admin/', include(admin.site.urls)),
]
