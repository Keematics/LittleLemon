from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
# from rest_framework.decorators import api_view
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer
# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer