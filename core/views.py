from django.shortcuts import render
import json
from core.models import Post, Comment
from core.forms import CommentForm
from django.views.generic import ListView
from django.http import Http404, HttpResponse
# Create your views here.

class Main(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'core/main.html'


def Detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    if request.is_ajax() and request.POST:
        text = request.POST.get('comment')
        comment = Comment(text=text, post=post)
        comment.save()
        data = {'message': request.POST.get('comment')}
        return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'core/detail.html', context)
