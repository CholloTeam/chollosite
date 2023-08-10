"""
URL configuration for chollosite project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chollo_cart', include('chollosite.chollo_cart.urls', namespace='chollo_cart')),
    path('orders', include('orders.urls', namespace='orders')),
    path('chollo_main/', include('chollosite.chollo_main.urls', namespace='chollo_main'))
]

# Make sure that you include this URL pattern before the shop.urls pattern, since it’s more restrictive
# than the latter.

# "namespace: app url name" = the url to use

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# In Production environment, Never serve static files with Django.
# You'll do it in going live

