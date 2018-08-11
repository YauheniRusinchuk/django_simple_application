from django.urls import path
from addpost.views import CreatePost


app_name = 'addpost'

urlpatterns = [
    path('', CreatePost.as_view(), name='addpost'),
]
