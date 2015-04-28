from django.contrib import admin
from tools.item_share.models import ItemModel, ItemSignupModel
from tools.allergy_list.models import AllergyModel
from tools.upload_pics.models import UploadedPicModel
from tools.weather.models import WeatherModel
from tools.ride_share.models import Car, Person, Riders
from tools.schedule.models import ScheduleModel
from tools.maps.models import Gmap
from tools.forum.models import ForumModel, ThreadModel, PostModel
from tools.money_share.models import MsSettingsModel, MsItemModel, MsSplitsModel, MsPaymentModel

admin.site.register(ItemModel)
admin.site.register(ItemSignupModel)
admin.site.register(AllergyModel)
admin.site.register(UploadedPicModel)
admin.site.register(WeatherModel)
admin.site.register(Car)
admin.site.register(Person)
admin.site.register(Riders)
admin.site.register(ScheduleModel)
admin.site.register(Gmap)
admin.site.register(ForumModel)
admin.site.register(ThreadModel)
admin.site.register(PostModel)
admin.site.register(MsSettingsModel)
admin.site.register(MsItemModel)
admin.site.register(MsSplitsModel)
admin.site.register(MsPaymentModel)
