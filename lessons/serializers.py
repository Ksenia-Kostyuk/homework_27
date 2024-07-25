from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from courses.models import Course


class LessonSerializer(ModelSerializer):
    course = SerializerMethodField()

    def get_course(self, course):
        return [cour.name for cour in Course.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'
