from django.contrib import admin

from shops import models


admin.site.register(models.Item)
admin.site.register(models.Shop)
