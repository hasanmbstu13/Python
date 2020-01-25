"""Views for Organizer App"""
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TagSerializer
from .models import Tag

class TagApiDetail(APIView):
    """Return JSON for single Tag object"""

    def get(self, request, slug):
        """Handle GET HTTP method"""

        # path parameter and api parameter sholud be same
        # like here in both cases we use slug
        # slug=slug first slug is the name of the model
        # and the slug is the name of the parameter
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = TagSerializer(
            tag,
            context={"request": request},
        )
        return Response(s_tag.data)


class TagApiList(APIView):
    """Return JSON for multiple Tag objects"""

    def get(self, request):
        """Handle GET HTTP method"""
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(
            tag_list,
            many=True,
            context={"request": request},
        )
        return Response(s_tag.data)
