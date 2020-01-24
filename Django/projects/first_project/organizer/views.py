import json

from django.http import Http404, HttpResponse

from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from django.views import View

from .models import Tag

def serialize_tag_to_dict(tag):
    return dict(
        id=tag.pk,
        name=tag.name,
        slug=tag.slug,
    )

def serialize_tag_to_json(tag):
    return json.dumps(serialize_tag_to_dict(tag))

def serialize_tag_list_to_json(tag_list):
    return json.dumps(
        list(map(serialize_tag_to_dict, tag_list))
    )

class TagApiDetail(View):

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag_json = serialize_tag_to_json(tag)
        return HttpResponse(
            tag_json,
            content_type="application/json"
        )


class TagApiList(View):

    def get(self, request):
        tag_list = get_list_or_404(Tag)
        if not tag_list:
            raise Http404()
        tag_json = serialize_tag_list_to_json(tag_list)
        return HttpResponse(
            tag_json,
            content_type="application/json"
        )