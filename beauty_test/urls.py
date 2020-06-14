from django.urls import path
from beauty_test.views import questions, results

urlpatterns = [
    path('questions', questions, name='questions'),
    path('results', results, name='results'),
]