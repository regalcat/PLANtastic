from django.contrib import admin
from tools.item_share.models import ItemModel, ItemSignupModel
from tools.allergy_list.models import AllergyModel
from tools.upload_pics.models import UploadedPicModel

admin.site.register(ItemModel)
admin.site.register(ItemSignupModel)
admin.site.register(AllergyModel)
admin.site.register(UploadedPicModel)

