def participation(request):
    return {
            'my_submissions': request.session.get('submissions', []),
            'my_votes': request.session.get('votes', []),
            'my_comments': request.session.get('comments', [])
            }
