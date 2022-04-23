
from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings


urlpatterns = [
    path('image_upload', views.upload_image_view, name = 'image_upload'),
    path('', views.event_view, name='event_view'),
    path('splash/', views.splash_view, name='splash_view'),
    path('login/', views.login_view, name='login_view'), 
    path('signup/', views.signup_view, name='signup_view'), 
    path('logout/', views.logout_view, name='logout_view')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
