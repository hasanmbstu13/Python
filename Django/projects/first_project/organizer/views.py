"""Views for Organizer App"""

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .models import Startup, Tag
from .serializers import StartupSerializer, TagSerializer

class TagApiDetail(RetrieveAPIView):
    """Return JSON for single Tag object"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class TagApiList(ListAPIView):
    """Return JSON for multiple Tag objects"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class StartupAPIDetail(RetrieveAPIView):
    """Handle GET HTTP method"""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"

class StartupAPIList(ListAPIView):
    """Return JSON for multiple Startup objects"""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
