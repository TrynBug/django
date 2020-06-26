from django.urls import path
from . import views


urlpatterns = [
    path('', views.important_words, name='important_words'),
]