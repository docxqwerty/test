from django.contrib import admin
from .models import Product, Lesson, Statistic, Access


class AccessAdm(admin.ModelAdmin):
    list_display = ('access', 'product', 'user')


admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Statistic)
admin.site.register(Access, AccessAdm)
