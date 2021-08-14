from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', views.UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='post-delete'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('post/<int:pk>/comment/', views.CreateCommentView.as_view(), name='comment-creation'),
    path('votes/<int:pk>', views.votesview, name='vote_post_view'),
]