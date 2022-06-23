# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('certificate/', include("apps.certify.urls")),
    path('accreditation/', include("apps.accreditation.urls")),
    path('tools/', include("apps.includes.sidebar.urls")),
    path('people/', include("apps.people.urls")),
    path('administration/', include("apps.administration.urls")),
    path('validations/', include("apps.validations.urls")),
    path('reports/', include("apps.reports.urls")),
    path('control/', include("apps.control.urls")),
    path('vehicles/', include("apps.vehicles.urls")),
    path('business/', include("apps.business.urls")),
    path('modules/', include("apps.modules.urls")),
    path('admin/', admin.site.urls),          # Django admin route
    path("login/", include("core.login.urls")), # Auth routes - login / register
    path("tablero/", include("apps.home.urls")),            # UI Kits Html files
    path("", include("apps.web.urls"))            # UI Kits Html files
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)