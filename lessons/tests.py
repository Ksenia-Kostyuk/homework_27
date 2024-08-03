from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Course
from lessons.models import Lesson
from users.models import User, Subscription


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='hatan@mail.ru')
        self.course = Course.objects.create(name='Дизайнер')
        self.lesson = Lesson.objects.create(name='Рисование', video='https://www.youtube.com/', course=self.course,
                                            owner=self.user)
        self.subcription = Subscription.objects.create(user=self.user, course=self.course)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('lessons:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEquals(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEquals(
            data.get('name'), self.lesson.name
        )

