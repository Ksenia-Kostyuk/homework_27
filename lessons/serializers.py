from rest_framework.serializers import ModelSerializer

from courses.models import Course


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
