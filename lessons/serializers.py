from rest_framework import serializers

from courses.models import Course
from lessons.models import Lesson
from lessons.validators import validate_acceptable_url


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField(read_only=True)
    video = serializers.URLField(validators=[validate_acceptable_url])

    def get_course(self, course):
        return [cour.name for cour in Course.objects.filter(name=course)]

    class Meta:
        model = Lesson
        fields = '__all__'
