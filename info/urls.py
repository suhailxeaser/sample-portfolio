from django.urls import path
from .import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about', views.aboutPage, name='aboutPage'),
    path('projects/', views.projectsPage, name='projectsPage'),
    path('contact/', views.contactPage, name='contactPage'),
    # path('projects/<str:slug>/', views.projectDetail, name='projectDetail'),
    # path('email', views.send_email, name='send_email'),
]
