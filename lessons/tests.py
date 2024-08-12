from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Course
from lessons.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='hatan2235@mail.ru')
        self.course = Course.objects.create(name='Дизайнер')
        self.lesson = Lesson.objects.create(name='Рисование', video='https://www.youtube.com/', course=self.course,
                                            owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_lessons_retrieve(self):
        url = reverse('lessons:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(data.get('name'), self.lesson.name)

    def test_lesson_create(self):
        url = reverse('lessons:lessons_list')
        data = {
            'name': 'Палитра',
            'video': 'https://www.youtube.com/',
            'course': self.course.name
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('lessons:lessons_retrieve')
        data = {
            'name': 'Палитра'
        }
        response = self.client.patch(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), 'Палитра')

    def test_lesson_delete(self):
        url = reverse('lessons:lessons_retrieve')
        response = self.client.patch(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_lesson_list(self):
        url = reverse('lessons:lessons_list')
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
