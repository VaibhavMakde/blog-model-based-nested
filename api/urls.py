from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet, AutherModelViewSet

router = DefaultRouter()

router.register('blog', PostModelViewSet)
router.register('author', AutherModelViewSet)

urlpatterns = [
    path('postapi/', include(router.urls)),

]
