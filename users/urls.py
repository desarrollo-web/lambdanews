from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('users.views',
    url(r'^login$', login, {'template_name' : 'users/login.html'}, name="login"),
    url(r'^logout$', logout,  {'next_page': '/'}, name="logout"),
    url(r'^register$', 'register', name="register"),
)
