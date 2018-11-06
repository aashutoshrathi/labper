from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from landing import views


admin.autodiscover()

urlpatterns = [
    url(r'^$', views.land, name='land'),
    url(r'^home/$', views.home, name='home'),
    url(r'^404/$', views.test_404, name='test_404'),
    url(r'^ide/$', views.ide, name='ide'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_course/', login_required(views.AddCourseView.as_view()), name='add_course'),
    url(r'^edit_course/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$',
        login_required(views.EditCourseView.as_view()), name='edit_course'),
    url(r'^course/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$',
        views.course_detail, name='course_detail'),
    url(r'^list_course/', login_required(views.ListCourseView.as_view()),
        name='list_course'),
    path('admin/', admin.site.urls),
    url(r'^logout/$', auth_views.LogoutView.as_view(
        template_name="registration/login.html"), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^teach/(?P<teacher>[\w\-]+)/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$',
        views.teach_course, name='teach'),
    url(r'^rm_std/(?P<student>[\w\-]+)/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$',
        views.remove_student, name='remove_student'),
    url(r'^rm_ta/(?P<assistant>[\w\-]+)/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$',
        views.remove_assistant, name='remove_ta'),
    url(r'^leave/(?P<teacher>[\w\-]+)/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$',
        views.leave_course, name='leave'),
    url(r'^add_lab/(?P<course>[\w\-]+)/(?P<session>[\w\-]+)/$',
        login_required(views.AddLabView.as_view()), name='add_lab'),
]
