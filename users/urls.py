from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from users.views import PaymentViewSet, UserCreateAPIView, SubscriptionAPIView, SubscriptionListAPIView, \
    SubscriptionRetrieveAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView, SubscriptionUpdateAPIView
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register('payment', PaymentViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('subscribe/', SubscriptionAPIView.as_view(), name='subscription-view'),
    path('subscribe/list/', SubscriptionListAPIView.as_view(), name='subscription-list'),
    path('subscribe/<int:pk>', SubscriptionRetrieveAPIView.as_view(), name='subscription-retrieve'),
    path('subscribe/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('subscribe/<int:pk>/delete/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'),
]

urlpatterns += router.urls
