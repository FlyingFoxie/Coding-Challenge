from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload.as_view(), name='upload'),
    path('list/', data_terminal_list, name='list'),
    path('data_terminal/', data_terminal_api_list.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)