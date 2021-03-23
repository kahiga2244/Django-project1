# from django.shortcuts import render
# from .models import Poll,User

# # Create your views here.
# def home(request):
#     context = {}
#     return render(request, 'home.html',context)

# def create(request):
#     form = CreatePollForm()
#     context = {'form' : form }
#     return render(request, 'create.html',context)

# def vote(request, poll_id):
#     context = {}
#     return render(request, 'vote.html', context)

# def results(request, poll_id):
#     context = {}
#     return render(request, 'results.html', context)


from django.shortcuts import render
from .models import Poll,User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html',context)

# def create(request):
#     # form = CreatePollForm()
#     context = {'form' : form }
#     return render(request, 'create.html',context)
@csrf_protect
def vote(request):
    context = {}
    return render(request, 'vote.html', context)

# def results(request, poll_id):
#     context = {}
#     return render(request, 'results.html', context)