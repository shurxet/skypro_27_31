from django.urls import path
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
]
