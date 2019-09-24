from django.contrib import admin
from django.urls import path, include

from searches.views import search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_view),
    path('', include('new_app.urls')),

]
