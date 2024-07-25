from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payment


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    filter_backends = [filters.OrderingFilter]
    filter_fields = ('course', 'lesson', 'method',)
    ordering_fields = ('date')
