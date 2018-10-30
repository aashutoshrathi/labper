from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from landing import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.land, name='land'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_course/', views.AddCourseView.as_view(), name='add_course'),
    url(r'^course/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$', views.course_detail, name='course_detail'),
    url(r'^list_course/', views.ListCourseView.as_view(), name='list_course'),
    path('admin/', admin.site.urls),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/login.html"), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^teach/(?P<teacher>[\w\-]+)/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$', views.teach_course, name='teach'),
    url(r'^leave/(?P<teacher>[\w\-]+)/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$', views.leave_course, name='leave'),
]
