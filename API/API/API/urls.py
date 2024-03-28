from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('slr/', include('slr.urls')),
    path('manipulate/', include('manipulate.urls')),
    path('regressions/', include('regressions.urls')),
]