from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/create/', views.movie_create, name='movie_create'),
    path('movie/<int:movie_id>/review/',
         views.review_create, name='review_create'),
]
