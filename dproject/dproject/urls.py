from django.contrib import admin
from django.urls import path, include

from product.views import StatisticPlatform, ProductAPIview, LessonAPIview, LessonProgressAPIview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('api/v1/lessonlist', LessonAPIview.as_view()),
    path('api/v1/statistic_platform', StatisticPlatform.as_view()),
    path('api/v1/products/<int:pk>/', ProductAPIview.as_view()),
    path('api/v1/fixprogress/', LessonProgressAPIview.as_view())

]
