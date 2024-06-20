from django.contrib import admin 
from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token

# Based on https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/
booking_list = views.BookingViewSet.as_view({
    'get': 'list'
})

urlpatterns = [ 
    path('', views.restaurant, name='index'),
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', booking_list, name='booking'),
    path('api-token-auth/', obtain_auth_token)
]