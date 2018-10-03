from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
import landing.views

admin.autodiscover()

urlpatterns = [
    url(r'^home$', login_required(landing.views.HomeView.as_view()), name='home'),
    url(r'^signup/$', landing.views.signup, name='signup'),
    url(r'^account/overview/$', login_required(landing.views.AccountOverview.as_view()), name='overview'),
    url(r'^settings/password/$', login_required(landing.views.PasswordChangeView.as_view()), name='password'),
    url(r'^settings/username/$', login_required(landing.views.ChangeUsername.as_view()), name='username'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name="landing/home.html"), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^account_activation_sent/$', landing.views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        landing.views.activate, name='activate'),
]
