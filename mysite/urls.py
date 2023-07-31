"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from filebrowser.sites import site
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

from ReRAM.views import base_views

# from ReRAM import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ReRAM/', include('ReRAM.urls')),
    path('MBE/', include('MBE.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
    path('summernote/', include('django_summernote.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


