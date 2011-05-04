from django.shortcuts import render_to_response, get_object_or_404, redirect
from news.models import Submission
from news.forms import SubmissionForm
from django.template import RequestContext

def list(request, by_popularity=False):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            s = form.save()
            return redirect('newest')
        else:
            return render_to_response('new.html', {'form': form}, context_instance=RequestContext(request))

    return render_to_response(
            'list.html',
            {'submissions': getattr(Submission.objects, 'popular' if by_popularity else 'all')()
                }
            )

def create(request): 
    return render_to_response(
                'new.html',
                {'form': SubmissionForm(), },
                context_instance=RequestContext(request)
            )

def show(request, s_id):
    submission = get_object_or_404(Submission, pk=s_id)
    return render_to_response(
             'show.html',
             {'submission': submission}
            )

def upvote(request, s_id):
    submission = get_object_or_404(Submission, pk=s_id)
    submission.upvote()
    return redirect(submission)
