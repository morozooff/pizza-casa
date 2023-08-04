from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import *
from django.urls import path, include

router = SimpleRouter()

router.register(r'products', ProductViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('', about, name = 'about'),
    path('catalog', ProductList.as_view(), name = 'catalog'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name = 'product-detail')
]

