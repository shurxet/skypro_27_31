from django.urls import path

from ads.views import category, ad, selection

urlpatterns = [
    path('cat/', category.CategoriesListView.as_view()),
    path('cat/<int:pk>/', category.category_detail_views),
    path('cat/create/', category.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', category.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', category.CategoryDeleteView.as_view()),

    path('ad/', ad.AdsListView.as_view()),
    path('ad/<int:pk>/', ad.AdDetailView.as_view()),
    path('ad/create/', ad.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', ad.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', ad.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', ad.ad_upload_image_view),

    path('selection/', selection.SelectionListView.as_view()),
    path('selection/<int:pk>/', selection.SelectionDetailView.as_view()),
    path('selection/create/', selection.SelectionCreateView.as_view()),
    path('selection/<int:pk>/update/', selection.SelectionUpdateView.as_view()),
    path('selection/<int:pk>/delete/', selection.SelectionDeleteView.as_view()),
]
