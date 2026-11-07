
from django.contrib import admin
from django.urls import path
from base.views import home, profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('panel/', profile)
]
