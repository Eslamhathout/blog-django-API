from django.urls import path, include
# from myblog.api.views import api_root, ArticleList, ArticleDetail, UserList, UserDetail


from myblog.api.views import ArticleViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns





# Using DefaultRouter
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


# # Using custom urlconf 

# article_list = ArticleViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# article_detail = ArticleViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


# urlpatterns = format_suffix_patterns([
#     path('', api_root),

#     path('articles/', article_list, name='article_list'),
#     path('articles/<int:pk>', article_detail, name='article_detail'),
#     path('users/', user_list, name='user_list'),
#     path('users/<int:pk>/', user_detail, name='user_detail'),

#     path('api-auth/', include('rest_framework.urls')),

# ])





# #Before using ViewSets
# urlpatterns = [
#     path('', api_root),

#     path('articles/', ArticleList.as_view(), name='article_list'),
#     path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
#     path('users/',UserList.as_view(), name='user_list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),

#     path('api-auth/', include('rest_framework.urls')),

# ]