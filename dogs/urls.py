from django.urls import path

from . import views



app_name = 'dogs'
urlpatterns = [
    path('breeds/', views.BreedList.as_view(), name='breeds'),
    path('breeds/<int:pk>/', views.BreedDetail.as_view()),
    path('dogs/', views.DogList.as_view(), name='breeds'),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),
]