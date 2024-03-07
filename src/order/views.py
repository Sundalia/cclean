from rest_framework import viewsets
from django.db.models import Prefetch
from .models import *
from .serializers import *

class OrderAPIView(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
class CleaningTypeAPIView(viewsets.ModelViewSet):
    queryset=CleaningType.objects.all()
    serializer_class=CleaninigTypeSerializer
    
class CleqaningTypeLocationAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeLocation.objects.all()
    serializer_class=CleaningTypeLocationSerializer
    
class CleaningTypeIncludeAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeInclude.objects.all()
    serializer_class=CleaningTypeIncludeSerializer
    
class CleaningTypeIncludeListAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeIncludeList.objects.all()
    serializer_class=CleaningTypeIncludeListSerializer
    
class CleaningTypeCanAddAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeCanAdd.objects.all()
    serializer_class=CleaningTypeCanAddSerializer
    
class CleaningTypeCanAddListAPIView(viewsets.ModelViewSet):
    queryset=CleaningTypeCanAddList.objects.all()
    serializer_class=CleaningTypeCanAddListSerializer
    
class FurnitureClutteredAPIView(viewsets.ModelViewSet):
    queryset=FurnitureCluttered.objects.all()
    serializer_class=FurnitureClutteredSerialier
    
class ThingsClutteredAPIView(viewsets.ModelViewSet):
    queryset=ThingsCluttered.objects.all()
    serializer_class=ThingsClutteredSerialier
    
class PollutionDegreeAPIView(viewsets.ModelViewSet):
    queryset=PollutionDegree.objects.all()
    serializer_class=PollutionDegreeSerialier
    
class ProomoAPIView(viewsets.ModelViewSet):
    queryset=Promo.objects.all()
    serializer_class=PromoSerializer
    
class OrderStatusAPIView(viewsets.ModelViewSet):
    queryset=OrderStatus.objects.all()
    serializer_class=OrderStatusSerializer