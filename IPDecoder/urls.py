from django.contrib import admin
from django.urls import path
from Decoder import views as decoder_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', decoder_views.index, name='index'),
]
