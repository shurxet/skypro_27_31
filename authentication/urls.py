from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import user

urlpatterns = [
    path('user/', user.UsersListView.as_view()),
    path('user/<int:pk>/', user.UserDetailView.as_view()),
    path('user/create/', user.UserCreateView.as_view()),
    path('user/<int:pk>/update/', user.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', user.UserDeleteView.as_view()),
    path('user/login/', views.obtain_auth_token),
    path('user/logout/', user.UserLogout.as_view()),
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
]