from django import forms

from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Postfields = '__all__'

  def clean_slug(self):
    return self.cleaned_data['slug'].lower
