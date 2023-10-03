from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Access, Product


def index(request):
    return HttpResponse('Hello')


class LessonAPIview(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        current_user = request.user
        products = Product.objects.filter().all()
        results = {}
        for product in products:
            access = Access.objects.filter(user=current_user.id, product_id=product.id)
            if access:
                lessons = product.lesson_set.all()
                ls_lessons = []
                for lesson in lessons:
                    statistic = lesson.statistic_set.first()
                    if statistic:
                        ls_lessons.append({'lesson': lesson.title,
                                           'status': statistic.status,
                                           'vieving_time': lesson.duration})
                results.update({product.title: ls_lessons})
        return Response(results)


class ProductAPIview(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        current_user = request.user
        access = Access.objects.filter(user=current_user.id, product_id=pk).first()
        if access:
            product = Product.objects.filter(pk=pk).first()
            lessons = product.lesson_set.all()
            ls_lessons = []
            for lesson in lessons:
                last_look_date = lesson.last_look_date
                statistic = lesson.statistic_set.first()
                if statistic:
                    ls_lessons.append({'lesson': lesson.title,
                                       'status': statistic.status,
                                       'vieving_time': statistic.viewing_time,
                                       'last_look': last_look_date})
            return Response({product.title: ls_lessons})
        else:
            return Response({'200': 'No access'})


class StatisticPlatform(APIView):
    def get(self, request):
        products = Product.objects.all()
        results = []
        for product in products:
            lessons = product.lesson_set.all()
            looks_lessons = sum([lesson.statistic_set.filter(status=True).count() for lesson in lessons])
            viewing_time = sum([sum([stat.viewing_time for stat in lesson.statistic_set.all()])
                                for lesson in lessons])
            have_access = product.access_set.filter(access=True).count()
            percent = products.count() * have_access * 100 / (User.objects.all().count() - 1)
            results.append({'Product': product.title,
                            'Look_lessons': looks_lessons,
                            'Viewing_time': viewing_time,
                            'Have_access': have_access,
                            'Percent': percent})
        return Response(results)
