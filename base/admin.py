from django.contrib import admin
from base.events.models import EventModel, HikeEventModel, GenericTripModel, GenericGatheringModel, InviteModel


admin.site.register(EventModel)
admin.site.register(HikeEventModel)
admin.site.register(GenericTripModel)
admin.site.register(GenericGatheringModel)
admin.site.register(InviteModel)


