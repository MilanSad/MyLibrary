from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

def home_page(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render({}, request))


@login_required
def profile(request):
  template = loader.get_template('404.html')

  return HttpResponse(template.render({'user': request.user}, request))
