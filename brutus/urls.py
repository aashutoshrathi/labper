from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from landing import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.land, name='land'),
    url(r'^home/$', views.home, name='home'),
    path('admin/', admin.site.urls),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/login.html"), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
