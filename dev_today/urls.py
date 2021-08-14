from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_board.urls')),
    path('', include('author_user.urls')),
    path('', include('rest_news.urls')),
    path('authors/', include('django.contrib.auth.urls')),
]
