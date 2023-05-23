from django.contrib import admin
from django.urls import path, include
from uploader.views import accounts_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uploader.urls')),
    path('dbf_upload/', include('uploader.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', accounts_view, name='accounts'),
]
