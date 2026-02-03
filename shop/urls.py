from django.contrib import admin
from django.urls import include, path
from main import views

urlpatterns = [
    path('', views.home, name='root'),
    path('admin/', admin.site.urls),

    # Main public pages
    path('home/', views.home, name='home'),
    path('collections/', views.collections, name='collections'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Users app (auth + products + orders)
    path('users/', include('users.urls')),

    # Admin dashboard
    path('adminapp/', include('adminapp.urls')),
]
