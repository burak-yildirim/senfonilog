from django.urls import path, include
from .api.router import router


" /blog/ "
urlpatterns = [
    path("", include(router.urls)),
]
