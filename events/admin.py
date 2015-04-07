from django.contrib import admin
from models import EventModel, HikeEventModel, GenericTripModel, GenericGatheringModel, DinnerEventModel

admin.site.register(EventModel)
admin.site.register(HikeEventModel)
admin.site.register(GenericTripModel)
admin.site.register(GenericGatheringModel)
admin.site.register(DinnerEventModel)
