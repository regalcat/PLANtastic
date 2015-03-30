from django.contrib import admin
from base.events.models import EventModel, HikeEventModel, GenericTripModel, GenericGatheringModel, InviteModel
from base.invite.models import MembershipModel


admin.site.register(EventModel)
admin.site.register(HikeEventModel)
admin.site.register(GenericTripModel)
admin.site.register(GenericGatheringModel)
admin.site.register(InviteModel)
admin.site.register(MembershipModel)


