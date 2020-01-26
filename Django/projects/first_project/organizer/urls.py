"""URL Configuration for Organizer App"""
from django.urls import path

from .views import (
	StartupAPIDetail,
	StartupAPIList,
	TagApiDetail, 
	TagApiList
)

urlpatterns = [
    path("tag/", TagApiList.as_view(), name="api-tag-list"),
    path(
        "tag/<str:slug>/",
        TagApiDetail.as_view(),
        name="api-tag-detail"
    ),
    path(
    	"startup/",
    	StartupAPIList.as_view(),
    	name="api-startup-list",
    ),
    path(
    	"startup/<str:slug>/",
    	StartupAPIDetail.as_view(),
    	name="api-startup-detail",
    ),
]