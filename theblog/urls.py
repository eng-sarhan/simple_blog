from django.urls import path, re_path

from . import views
from .views import ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, HomeView, LikeView, \
    CategoryListView, AddCategoryView, UserPostListView

app_name = 'theblog'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),

    path('categories/<str:cats>/', CategoryView, name='categories'),

    path("author/<int:author_id>/", views.PostListAuthor.as_view(), name="author"),

    path('category-list/', CategoryListView, name='category-list'),

    path('like/<int:pk>', LikeView, name='like_post'),

    re_path(r'^user/(?P<username>\w{0,50})/$', UserPostListView.as_view(), name='user-posts'),

    # path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
