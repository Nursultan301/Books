from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from store.views import BookViewSet

router = SimpleRouter()

router.register(r'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
