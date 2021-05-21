from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")

urlpatterns = [
    path("hello-apiview/", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]
