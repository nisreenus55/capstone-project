from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes, parser_classes
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
# Create your views here.
from django.http import HttpResponse
#in views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
# def sayHello(request):
#     return HttpResponse('Hello World')

# def index(request):
#     return render(request, 'index.html', {})



# class RetrieveUpdateUserAPIView(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'

# class RetrieveDestroyUserAPIView(generics.RetrieveDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'


# class ListUserAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class CreateUserAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer   

# class RetrieveUserAPIView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer 
#     lookup_field = 'username'

# class UpdateUserAPIView(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer 
#     lookup_field = 'username'

# class DestroyUserAPIView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer 
#     lookup_field = 'username'

# class bookingview(APIView):

#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)

#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({"data":serializer.data, "status": "success"})
    
# class menuview(APIView):

#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = MenuSerializer(items, many=True)

#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({"data":serializer.data, "status": "success"})

# class BookingsView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

# class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#     lookup_field = 'first_name'

# User CRUD APIs
class ListCreateUserAPIView(generics.ListCreateAPIView):  #It handles POST,GET
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 

class RetrieveUpdateDestroyUserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated] 

# Menu CRUD APIs
class MenuItemsView(generics.ListCreateAPIView): # POST,GET
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):  #GET, PUT and DELETE , NO POST, NO PATCH
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):  #GET, PUT and DELETE , NO POST, NO PATCH

    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # lookup_field = 'title'

# Booking CRUD APIs
class BookingViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer