from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication import views_user


urlpatterns = [
    path('user/', views_user.UsersListView.as_view()),
    path('user/<int:pk>/', views_user.UserDetailView.as_view()),
    path('user/create/', views_user.UserCreateView.as_view()),
    path('user/<int:pk>/update/', views_user.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views_user.UserDeleteView.as_view()),
    path('user/login/', views.obtain_auth_token),
    path('user/logout/', views_user.UserLogout.as_view()),
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
]