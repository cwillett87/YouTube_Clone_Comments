from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('comments/<int:pk>/<str:video_id>/', views.CommentLike.as_view()),
    path('comments/<int:pk>/<int:likes>/', views.CommentDislike.as_view()),
]
