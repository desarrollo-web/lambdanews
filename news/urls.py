from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'^$', 'list', {'popular_first': True}, name="popular"),
    url(r'^newest$', 'list', name='newest'),
    url(r'^new$', 'create', name='create'),

    url(r'^(?P<s_id>\d+)', 'show', name='show'),
    url(r'^(?P<s_id>\d+)/upvote$', 'upvote', name='upvote'),

    url(r'^(?P<s_id>\d+)/comments', 'comment', name='add_comment'),
    url(r'^(?P<s_id>\d+)/comments/(?P<c_id>\d+)', 'reply', name='reply_to_comment'),
)
