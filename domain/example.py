from data.models import TestModel


def get(obj_id):
    return TestModel.objects.get(id=obj_id)
