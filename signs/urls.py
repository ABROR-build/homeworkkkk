from django.urls import path
from . import views


urlpatterns = [
    path('list-categories', views.CategoryListAPIView.as_view(), name='list-categories'),
    path('list-signs', views.SignsListAPIView.as_view(), name='list-signs')
]
