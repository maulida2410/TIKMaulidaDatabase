
from django.contrib import admin
from django.urls import path
from seputaruntirta.views import untirtajwr


urlpatterns = [
    path('admin/', admin.site.urls),
    path('seputaruntirta/', untirtajwr),
]   

