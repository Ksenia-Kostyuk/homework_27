from rest_framework.routers import SimpleRouter

from courses.views import CourseViewSet
from lessons.apps import LessonsConfig

app_name = LessonsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)


urlpatterns = []

urlpatterns += router.urls