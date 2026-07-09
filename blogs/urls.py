from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blogpost_list'),
    path('create/', views.BlogPostCreateView.as_view(), name='blogpost_create'),
    path('<int:pk>/', views.BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('<int:pk>/update/', views.BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('<int:pk>/delete/', views.BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('drafts/', views.BlogPostDraftListView.as_view(), name='blogpost_draft_list'),
    path('<int:pk>/publish/', views.BlogPostPublishView.as_view(), name='blogpost_publish'),
]