from django.contrib import admin
from django.urls import path, include
from bookings import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.home, name='home'),
=======
    path('', views.main, name='home'),
>>>>>>> 9707b91aa08f71c60f8b3f3b605d7bd060254610
    path('accounts/', include('accounts.urls')),
    path('bookings/', include('bookings.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
