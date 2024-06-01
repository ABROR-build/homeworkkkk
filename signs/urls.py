from django.urls import path
from . import views


urlpatterns = [
    path('categories-list/', views.CategoryListAPIView.as_view(), name='list-categories'),
    path('signs-list/', views.SignsListAPIView.as_view(), name='list-signs'),
    path('signs-detail/<int:pk>/', views.SignsDetailView.as_view(), name='detail-signs'),
    path('signs-delete/<int:pk>/', views.SignsDeleteView.as_view(), name='delete-signs'),
    path('signs-put/<int:pk>/', views.SignsPutView.as_view(), name='put-signs'),
    path('signs-create/', views.SignsCreateView.as_view(), name='create-signs'),
]
