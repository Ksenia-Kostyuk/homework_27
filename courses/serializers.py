from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons = LessonSerializer()

    class Meta:
        model = Course
        fields = ('name', 'description', 'get_lessons_count')

    def get_lessons_count(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

