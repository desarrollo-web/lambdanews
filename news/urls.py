from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('lambdanews.news.views',
    url(r'^$', 'list', {'by_popularity': True}, name="popular"),
    url(r'^newest$', 'list', name='newest'),
    url(r'^new$', 'create', name='create'),

    url(r'^(?P<s_id>\d+)$', 'show', name='show'),
    url(r'^(?P<s_id>\d+)/upvote$', 'upvote', name='upvote'),

    url(r'^(?P<s_id>\d+)/comments$', 'comment', name='add_comment'),
)
