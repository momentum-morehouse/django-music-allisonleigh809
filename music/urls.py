"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import registration
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from musiclist import views as musiclist_views

urlpatterns = [
  path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('', musiclist_views.list_albums,
    name='list_albums'), 
    path('albums', musiclist_views.list_albums, name='list_albums'),
    path('albums/add', musiclist_views.add_albums, name='add_albums'),
    path('albums/<int:pk>/delete/', musiclist_views.delete_albums, name='delete_albums'),
    path('albums/<int:pk>/edit/',musiclist_views.edit_albums, name='edit_albums'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
