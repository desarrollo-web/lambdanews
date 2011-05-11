from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            user = f.save()
            authenticated = authenticate(username = user.username, password = f.cleaned_data['password1'])
            login(request, authenticated)
            return redirect('homepage')
        else:
            return render_to_response('register.html',
                                      {'form': f },
                                        context_instance=RequestContext(request))
    return render_to_response('register.html', {'form':UserCreationForm()}, context_instance=RequestContext(request))
