from django import forms
from .models import Posts
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Posts
        fields = "__all__"
