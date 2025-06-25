from django.urls import path
from .views import SignupView, LoginView, CommentView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('comments/', CommentView.as_view(), name='comment'),
]