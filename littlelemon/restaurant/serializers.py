from rest_framework import serializers, fields
from django.contrib.auth.models import User

from .models import Menu, Booking
from decimal import Decimal
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        # fields = ['id', 'title', 'price',  'inventory']
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'

        fields = [ 'username', 'first_name', 'last_name','email', 'groups']



# class MenuItemView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = MenuItem.objects.select_related('category').all()
#     serializer_class = MenuItemSerializer

    
    
# class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = MenuItem.objects.select_related('category').all()
#     serializer_class = MenuItemSerializer
