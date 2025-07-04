from django.urls import path
from .views import SignupView, LoginView, CommentView, ReviewView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('comments/', CommentView.as_view(), name='comment'),
    path('reviews/', ReviewView.as_view(), name='review'),
]