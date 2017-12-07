from django.shortcuts import render

# Create your views here.
def polls(request):
    context = {}
    template = 'polls.html'
    return render(request,template,context)
