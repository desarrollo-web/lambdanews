from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to, direct_to_template
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', redirect_to, {'url': '/submissions', 'permanent': False}, name="homepage"),
    (r'^examen$', direct_to_template, {'template': 'examen.html'}),
    (r'^submissions/', include('lambdanews.news.urls')),

    #users
    url(r'^users/login$', login, {'template_name' : 'users/login.html'}, name="login"),
    url(r'^users/logout$', logout,  {'next_page': '/'}, name="logout"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
