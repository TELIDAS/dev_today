from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/post/', views.PostGenericAPIView.as_view(), name='post_generic'),
    path('api/post/<int:id>/', views.PostGenericDetailAPIView.as_view(), name='post_generic_detail'),
    path('api/register/', views.RegisterAPIView.as_view(), name='register-generic'),
    path('api/users/', views.UserList.as_view(), name='user-list-generic'),
    path('api/users/<int:id>/', views.UserDetail.as_view(), name='user-list-generic'),
    path('api/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/token-verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('api/comment/', views.CommentGenericAPIView.as_view(), name='comment_generic'),
    path('api/comment/<int:id>/', views.CommentGenericDetailAPIView.as_view(), name='comment_generic_detail'),

]
