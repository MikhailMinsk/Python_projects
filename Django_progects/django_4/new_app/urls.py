from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.blog_list, name='home'),
    path('create/', views.blog_create, name='create'),
    path('<str:slug>/delete/', views.blog_delete, name='delete'),
    path('<str:slug>/update/', views.blog_update, name='update'),
    # path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<str:slug>/', views.blog_detail, name='detail'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
