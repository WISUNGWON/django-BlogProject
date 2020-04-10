from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:blog_id>', views.detail, name='detail'),
    path('blog/new', views.new, name='new'),
    path('blog/create', views.create, name='create'),
]
