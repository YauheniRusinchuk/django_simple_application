from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from addpost.forms import PostForm

class CreatePost(CreateView):
    template_name = 'addpost/addpost.html'
    form_class = PostForm
    success_url = reverse_lazy('core:main')
