from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('logout/',views.user_login, name='logout'),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('edit/<int:image_id>/', views.edit_image, name='edit_image'),

]