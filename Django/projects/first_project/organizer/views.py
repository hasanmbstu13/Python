"""Views for Organizer App"""
import json

from django.http import Http404, HttpResponse

from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from django.views import View
from rest_framework.renderers import JSONRenderer

from .serializers import TagSerializer
from .models import Tag

class TagApiDetail(View):
    """Return JSON for single Tag object"""

    def get(self, request, pk):
        """Handle GET HTTP method"""
        tag = get_object_or_404(Tag, pk=pk)
        s_tag = TagSerializer(tag)
        tag_json = JSONRenderer().render(s_tag.data)
        return HttpResponse(
            tag_json,
            content_type="application/json"
        )


class TagApiList(View):
    """Return JSON for multiple Tag objects"""

    def get(self, request):
        """Handle GET HTTP method"""
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(tag_list, many=True)
        tag_json = JSONRenderer().render(s_tag.data)
        return HttpResponse(
            tag_json,
            content_type="application/json"
        )