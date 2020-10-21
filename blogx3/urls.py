from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>',views.post_id, name='post'),
    path('post',views.posts, name='all_posts'),
]