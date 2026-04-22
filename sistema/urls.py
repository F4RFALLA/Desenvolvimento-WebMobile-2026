from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sistema.views import Login, Home, Logout

urlpatterns = [
    path('', Login.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('veiculo/', include('veiculo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
