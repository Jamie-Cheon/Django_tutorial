from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]




















# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from .views import SnippetViewSet, UserViewSet
#
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = UserViewSet.as_view({
#     'get': 'list',
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve',
# })
#
#
# urlpatterns = format_suffix_patterns([
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
# ])
#



# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns((urlpatterns))
