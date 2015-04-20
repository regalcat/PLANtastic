from django.contrib import admin
from tools.item_share.models import ItemModel, ItemSignupModel
from tools.allergy_list.models import AllergyModel
from tools.upload_pics.models import UploadedPicModel
from tools.weather.models import WeatherModel
from tools.ride_share.models import RideModel, RideSignupModel

admin.site.register(ItemModel)
admin.site.register(ItemSignupModel)
admin.site.register(AllergyModel)
admin.site.register(UploadedPicModel)
admin.site.register(WeatherModel)
admin.site.register(RideModel)
admin.site.register(RideSignupModel)

