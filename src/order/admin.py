from django.contrib import admin
from .models import *

admin.site.register(CleaningType)
admin.site.register(CleaningTypeLocation)
admin.site.register(CleaningTypeInclude)
admin.site.register(CleaningTypeIncludeList)
admin.site.register(CleaningTypeCanAdd)
admin.site.register(CleaningTypeCanAddList)
admin.site.register(FurnitureCluttered)
admin.site.register(ThingsCluttered)
admin.site.register(PollutionDegree)
admin.site.register(Promo)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(FeedBack)
