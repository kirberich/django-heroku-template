from django.contrib import admin
from data.models import TestModel


class TestModelAdmin(admin.ModelAdmin):
    class Meta:
        verbose_app_name = 'Testing'

admin.site.register(TestModel, TestModelAdmin)
