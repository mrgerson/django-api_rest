from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusinessViewSet, DependenceViewSet, BusinessDependenceViewSet

router = DefaultRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'dependences', DependenceViewSet)
router.register(r'business-dependences', BusinessDependenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('businesses/<int:pk>/sync-dependences/', BusinessDependenceViewSet.as_view({'post': 'sync_dependences'})),
]