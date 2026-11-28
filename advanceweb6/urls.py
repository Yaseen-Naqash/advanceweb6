
from django.contrib import admin
from django.urls import path
from base.views import home, profile, detail, products
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('panel/', profile),
    path('detail/<int:pk>/', detail, name='detail_url'),
    path('products/', products)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)