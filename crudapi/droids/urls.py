from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateDroidAPIView.as_view(), name='get_post_Droids'),
    path('<int:pk>/', views.RetrieveUpdateDestroyDroidAPIView.as_view(), name='get_delete_update_Droid'),
]