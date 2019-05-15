"""image_upload_return URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from upload import views
#from upload.urls import router as upload_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get', views.ImageGet.as_view(), name='image-get'),
    url(r'^set', views.ImageSet.as_view(), name='image-set'),
    #url(r'^api/', include(upload_router.urls)),
]
