from django.contrib import admin

from .models import Setting, Vkcity, Vkuser, Vkpost
from .models import Url, Group_found, Filter

admin.site.register(Setting)
admin.site.register(Vkcity)
admin.site.register(Vkuser)
admin.site.register(Vkpost)

admin.site.register(Url)
admin.site.register(Group_found)
admin.site.register(Filter)




# Register your models here.
