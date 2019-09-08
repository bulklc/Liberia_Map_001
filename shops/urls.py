from django.urls import path

from shops import apps
from shops import views


app_name = apps.ShopsConfig.name

urlpatterns = [
    path('', views.MapTemplateView.as_view(), name='map'),
]
