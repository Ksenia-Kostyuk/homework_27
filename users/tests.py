from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from courses.models import Course
from lessons.models import Lesson
from users.models import User, Subscription


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='hatan2235@mail.ru')
        self.course = Course.objects.create(name='Дизайнер')
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('users:subscription-create')
        data = {
            "user": self.user,
            "course": self.course
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_list(self):
        url = reverse('users:subscription-list')
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription_retrieve(self):
        url = reverse('users:subscription-retrieve', args=(self.subscription.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_subscription_delete(self):
        url = reverse('users:subscription-delete')
        response = self.client.patch(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
