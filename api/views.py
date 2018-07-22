from rest_framework.generics import ListAPIView
from .serializers import RestaurantsListSerializer
from restaurants.models import Restaurant

# Complete me! I should be your APIListView
class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantsListSerializer
	