from django.http import HttpResponse
from django.views.decorators.http import (
    require_http_methods
)

@require_http_methods(["GET", "HEAD"])
def hello_world(request):
    return HttpResponse("Hello world!")