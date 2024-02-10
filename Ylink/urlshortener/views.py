from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LinkForm
# Create your views here.

from .models import Links

def home_view(request):
    context={}
    template='home.html'
    
    context['form'] = LinkForm()
    
    allLinks = Links.objects.all()
    context['allLinks'] = allLinks
    context['domain'] = request.build_absolute_uri('/')
    if request.method=='GET':
        return render(request, template, context)
    
    elif request.method=='POST':
        form = LinkForm(request.POST)
        
        if form.is_valid():
            link = form.save(commit=False)
            link.save()
            context['shortened_url'] = request.build_absolute_uri('/') + link.short
            context['link'] = link.link
            context['form'] = LinkForm()
            return render(request, template, context)

        context['errors'] = form.errors
        return render(request, template, context)
     

def redirect_view(request, shortlink):
    try:
        link = get_object_or_404(Links, short=shortlink)
        link.visits += 1
        link.save()
        return HttpResponseRedirect(link.link)
    except:
        return HttpResponse('Invalid URL')