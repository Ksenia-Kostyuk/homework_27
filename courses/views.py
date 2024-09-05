from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from courses.models import Course
from courses.paginations import CustomCoursesPagination
from courses.serializers import CourseSerializer
from users.models import Subscription
from users.permissions import IsModerator, IsOwner
from courses.tasks import send_information_about_update_course


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="description from swagger_auto_schema via method_decorator"
))
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomCoursesPagination

    def perform_update(self):
        course = self.get_object()
        subscriptions = Subscription.objects.filter(course=course)
        if course.update.exists():
            for subscription in subscriptions:
                user = subscription.user.email
                send_information_about_update_course.delay(user)
        serializer = self.get_serializer(course)
        return Response(serializer.data)

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModerator,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()
