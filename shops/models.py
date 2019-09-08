from django.db import models


class Shop(models.Model):
    name = models.CharField(
        max_length=256,
    )

    latitude = models.DecimalField(
        max_digits=17,
        decimal_places=15,
    )

    longitude = models.DecimalField(
        max_digits=17,
        decimal_places=15,
    )

    items = models.ManyToManyField('shops.Item')

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "type": "Feature",
            "properties": {
                "Shop Name": self.name,
                "Items": [],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(self.latitude),
                    float(self.longitude),
                ]
            }
        }


class Item(models.Model):
    name = models.CharField(
        max_length=256,
    )

