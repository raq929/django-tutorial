from django.shortcuts import (
  get_object_or_404, redirect, render)
from django.template import Context, loader
from django.views.generic import View

from django.http.response import HttpResponse
from .models import Startup, Tag
from .forms import NewsLinkForm, TagForm, StartupForm
from .utils import ObjectCreateMixin

class NewsLinkCreate(ObjectCreateMixin, View):
  form_class = NewsLinkForm
  template_name = 'organizer/newslink_form.html'

def tag_list(request):
  return render(
    request,
    'organizer/tag_list.html',
    {'tag_list': Tag.objects.all() })

def tag_detail(request, slug):
  tag = get_object_or_404(Tag, slug__iexact=slug)
  return render(request,
    'organizer/tag_detail.html',
    { 'tag': tag })

class TagCreate(ObjectCreateMixin, View):
  form_class = TagForm
  template_name = 'organizer/tag_form.html'

class StartupCreate(ObjectCreateMixin, View):
  form_class = StartupForm
  template_name = 'organizer/startup_form.html'

def startup_list(request):
  return render(
    request,
    'organizer/startup_list.html',
    {'startup_list': Startup.objects.all() })

def startup_detail(request, slug):
  startup = get_object_or_404(Startup, slug__iexact=slug)
  return render(request,
    'organizer/startup_detail.html',
    { 'startup': startup })
