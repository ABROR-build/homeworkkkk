from django.urls import path
from . import views


urlpatterns = [
    path('signs-create/', views.CreateApiView.as_view(), name='Create API'),
    path('signs-get/', views.get, name = 'get')
]
