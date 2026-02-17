from django.urls import path
from . import views

urlpatterns = [
    path('orders/ingest/', views.OrderIngestAPIView.as_view(), name='order-ingest'),
]