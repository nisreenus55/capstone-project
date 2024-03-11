from django.contrib import admin 
from django.urls import path, include
from rest_framework import routers
from . import views 

# router = routers.DefaultRouter()
# router.register(r'users', views.userViewSet)
urlpatterns = [ 
    path('users/', views.ListCreateUserAPIView.as_view(), name='list-users'),
    path('users/<username>/', views.RetrieveUpdateDestroyUserAPIView.as_view(), name='destroy-users'),

    # path('bookings/', views.BookingsView.as_view(), name='list-bookings'),
    # path('bookings/<first_name>/', views.SingleBookingView.as_view(), name='RUD-bookings'),

    path('menu/', views.MenuItemsView.as_view(), name='list-menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='RUD-menu'),

    # path('book/', views.bookingview.as_view(), name='bookingview'),
    # path('menu/', views.bookingview.as_view(), name='menuview'),
    # path('users/<username>/', views.RetrieveUpdateUserAPIView.as_view(), name='update-users'),

    # path('users/list/', views.ListUserAPIView.as_view(), name='list-users'),
    # path('users/create/', views.CreateUserAPIView.as_view(), name='create-users'),
    # path('users/retrieve/<username>/', views.RetrieveUserAPIView.as_view(), name='retrieve-users'),
    # path('users/update/<username>/', views.UpdateUserAPIView.as_view(), name='update-users'),
    # path('users/destroy/<username>/', views.DestroyUserAPIView.as_view(), name='destroy-users'),

    
    # path('', include(router.urls)),



]

# urlpatterns += router.urls
