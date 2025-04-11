from django.contrib import admin
from django.urls import path
from GalakPage.views import RenderMainPage
from .views import noadmin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', noadmin),
    path('', RenderMainPage)
]
