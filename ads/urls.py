from django.urls import path
from ads import views_ads, views_users


urlpatterns = [
    path('cat/', views_ads.CategoriesListView.as_view()),
    path('cat/<int:pk>/', views_ads.CategoryDetailViews.as_view()),
    path('cat/create/', views_ads.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', views_ads.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views_ads.CategoryDeleteView.as_view()),

    path('ad/', views_ads.AdsListView.as_view()),
    path('ad/<int:pk>/', views_ads.AdDetailView.as_view()),
    path('ad/create/', views_ads.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', views_ads.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views_ads.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views_ads.AdUploadImageView.as_view()),

    path('user/', views_users.UsersListView.as_view()),
    path('user/<int:pk>/', views_users.UserDetailView.as_view()),
    path('user/create/', views_users.UserCreateView.as_view()),
    path('user/<int:pk>/update/', views_users.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views_users.UserDeleteView.as_view()),
]
