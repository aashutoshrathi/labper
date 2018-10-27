from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from landing import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.land, name='land'),
    url(r'^home/$', views.home, name='home'),
    url(r'^upgrade/', views.upgrade, name='upgrade'),
    url(r'^add_course/', views.AddCourseView.as_view(), name='add_course'),
    url(r'^list_course/', views.ListCourseView.as_view(), name='list_course'),
    path('admin/', admin.site.urls),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/login.html"), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
