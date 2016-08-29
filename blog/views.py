from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from .forms import PostForm
from .models import Post


class PostCreate(View):
  form_class = PostForm
  template_name = 'blog/post_form.html'

  def get(self, request):
    return render(
      request,
      self.template_name,
      {'form': self.form_class() })
  def post(self, request):
    if bound_form.is_valid():
        new_post = bound_form.save()
        return redirect(new_post)
    else:
      return render(
        request,
        self.template_name,
        { 'form': bound_form  })

class PostList(View):

  def get(self, request):
    return render(
      request,
      'blog/post_list.html',
      {'post_list': Post.objects.all() })

def post_detail(request, year, month, slug, parent_template=None):
  post = get_object_or_404(
    Post,
    pub_date__year=year,
    pub_date__month=month,
    slug=slug)
  return render(request,
    'blog/post_detail.html',
    { 'post': post })
