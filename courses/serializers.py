from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course
from lessons.models import Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = ('name', 'description', 'get_lessons_count', 'lessons')

    def get_lessons_count(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

    def lessons(self, lessons):
        return Lesson.objects.filter(name=lessons.name)
