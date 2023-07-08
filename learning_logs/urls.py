"""Defines URL patterns for learning_logs"""
from django.urls import path
from . import views
from .views import UpdatePostView

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    #path('', views.index, name='index'),
    # Page that shows all topics.
    
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    path('', views.index, name="index"),
    #path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),
]