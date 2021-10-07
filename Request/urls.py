from django.urls import path,include
from Request import views

urlpatterns = [
    path('requests/', views.RequestList.as_view()),
    path('requests/<int:pk>/', views.RequestDetail.as_view()),
]

