from django.contrib import admin
from django.contrib.auth.models import Group
from interfaces.admin.test_model import TestModelAdmin

admin.site.unregister(Group)

__all__ = [
    TestModelAdmin,
]
