from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class MapTemplateView(TemplateView):
    template_name = 'shops/index.html'


class PointListView(JSONResponseMixin, ListView):
    """
    Return JSON array of points. One point for each shop.


        [
          {
            "type": "Feature",
            "properties": {
              "Shop Name": "1",
              "Items": [],
            },
            "geometry": {
              "type": "Point",
              "coordinates": [
                -9.9376387894872,
                6.814259060308
              ]
            }
          }
        ]
    """
    def get_data(self, context):
        return [
          {
            "type": "Feature",
            "properties": {
              "Shop Name": "1",
              "Items": [],
            },
            "geometry": {
              "type": "Point",
              "coordinates": [
                -9.9376387894872,
                6.814259060308
              ]
            }
          }
        ]

