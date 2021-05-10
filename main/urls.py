from django.urls import path
from . import views

urlpatterns = [
    path("", views.TestRoute.as_view()),
    path("diabetes/", views.DiabetesAPIView.as_view()),
    path("liver/", views.LiverAPIView.as_view()),
    path("kidney/", views.KidneyAPIView.as_view()),
    path("malaria/", views.MalariaAPIView.as_view()),
    path("pneumonia/", views.PneumoniaAPIView.as_view()),
    path("skin/", views.SkinAPIView.as_view()),
    path("chat/", views.ChatBotAPIView.as_view()),
    path("nearbyHospitals/", views.GetNearbyDoctors.as_view()),
]