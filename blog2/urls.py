"""blog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index,name='index'),
    path('', views.index.as_view(),name='index' ),
    #path('blog', views.blog,name='blog'),
    path('blog/<int:pk>',views.blog.as_view(),name='blog'),
    #path('about/', views.about,name='about'),
    #path('<slug:slug>/',views.about.as_view(),name='about'),
    path('about/<int:pk>',views.about.as_view(),name='about'),
    #path('contact/', views.contact,name='contact'),
    path('contact/',views.listContect.as_view(),name='contact'),
    #path('features/', views.features,name='features'),
    path('features/<int:pk>',views.features.as_view(),name='features'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
