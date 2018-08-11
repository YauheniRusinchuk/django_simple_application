from django.urls import path, re_path
from core.views import Main, Detail

app_name = 'core'

urlpatterns = [
    path('post/<int:pk>/', Detail, name='detail'),
    path('', Main.as_view(), name='main'),
]
