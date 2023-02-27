from django.urls import path
<<<<<<< HEAD
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
=======
from ads import views_ad, views_selection, views_category

urlpatterns = [
    path('cat/', views_category.CategoriesListView.as_view()),
    path('cat/<int:cat_id>/', views_category.category_detail_Views),
    path('cat/create/', views_category.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', views_category.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views_category.CategoryDeleteView.as_view()),

    path('ad/', views_ad.AdsListView.as_view()),
    path('ad/<int:pk>/', views_ad.AdDetailView.as_view()),
    path('ad/create/', views_ad.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', views_ad.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views_ad.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views_ad.AdUploadImageView.as_view()),

    path('selection/', views_selection.SelectionListView.as_view()),
    path('selection/<int:pk>/', views_selection.SelectionDetailView.as_view()),
    path('selection/create/', views_selection.SelectionCreateView.as_view()),
    path('selection/<int:pk>/update/', views_selection.SelectionUpdateView.as_view()),
    path('selection/<int:pk>/delete/', views_selection.SelectionDeleteView.as_view()),
>>>>>>> b7ed7a2 (first commit)
]
