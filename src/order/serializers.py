from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=(
            '''в последующем можно изменить запись полей на `__all__`'''
            'customer', 
            'cleaning_type', 
            'square', 
            'furniture_cluttered', 
            'things_cluttered', 
            'pollution_degree',
            'room_choices',
            'cleaning_date',
            'cleaning_time',
            'photo',
            'window_clean',
            'address',
            'comment',
            'promo',
            'price',
            'created',
            'updated',
            'is_published',
            'cleaners_photo'
        )
        
        
class FurnitureClutteredSerialier(serializers.ModelSerializer):
    class Meta:
        model=FurnitureCluttered
        fields=(
            'name',
            'description',
            'created',
            'updated',
            'is_published'
        )
        
class ThingsClutteredSerialier(serializers.ModelSerializer):
    class Meta:
        model=ThingsCluttered
        fields=(
            'name',
            'description',
            'created',
            'updated',
            'is_published'
        )
        
class PollutionDegreeSerialier(serializers.ModelSerializer):
    class Meta:
        model=PollutionDegree
        fields=(
            'name',
            'description',
            'created',
            'updated',
            'is_published'
        )
        
class  PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Promo
        fields=(
            'name',
            'description',
            'price',
            'promocode',
            'cleaning_type',       
            'created',
            'updated',
            'is_published'
        )
        
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderStatus
        fields=(
            'order',
            'is_confirmed',
            'is_started',
            'is_finished',
            'is_paid'
        )
        
class CleaningTypeIncludeSerializer(serializers.ModelSerializer):
    
    include_list=serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        read_only=True
    )
    
    
    class Meta:
        model=CleaningTypeInclude
        fields=(
            'name',
            'include_list',
            'created',
            'updated',
            'is_published'
        )
        
class CleaningTypeIncludeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CleaningTypeIncludeList
        fields=(
            'cleaning_type_include',
            'name',
            'created',
            'updated',
            'is_published'
        )
        
class CleaningTypeCanAddSerializer(serializers.ModelSerializer):
    
    can_add_list=serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        read_only=True
    )    

    class Meta:
        model=CleaningTypeCanAdd
        fields=(
            'name',
            'price',
            'can_add_list',
            'created',
            'updated',
            'is_published'
        )
        
class CleaningTypeCanAddListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CleaningTypeCanAddList
        fields=(
            'can_add',
            'name',
            'created',
            'updated',
            'is_published'
        )
        
        
        
class CleaningTypeLocationSerializer(serializers.ModelSerializer):
    include=CleaningTypeIncludeSerializer(
        many=True
    )
    
    can_add=CleaningTypeCanAddSerializer(
        many=True
    ) 
    
    class Meta:
        model=CleaningTypeLocation
        fields=(
            'cleaning_type',
            'name',
            'subname',
            'include',
            'can_add',
            'created',
            'updated',
            'is_published'
        )
        
        
        
class  CleaninigTypeSerializer(serializers.ModelSerializer):
    location=CleaningTypeLocationSerializer(
        many=True
    )
    
    class Meta:
        model=CleaningType
        fields=(
            'name',
            'description',
            'location',
            'price',
            'created',
            'updated',
            'is_published'
    )
        