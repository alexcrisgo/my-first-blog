from django.shortcuts import render
from django.utils import timezone
from blog.models import Post #la palabra blog es opcional

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts})
