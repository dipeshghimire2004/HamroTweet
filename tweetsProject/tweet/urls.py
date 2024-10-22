from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'), 
    path('', views.tweet_List, name='tweet_List' ),
    # path('search_results/', views.search_results, name="search_results"),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register')  
] 