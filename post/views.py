from django.shortcuts import render
from .forms import PostForm

def pageform(request):
    form  = PostForm(request.POST or None)
    if form.is_valid():
        pass
    context = {'form': form}
    return render(request, 'pageform.html', context)
