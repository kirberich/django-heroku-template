from django.http import JsonResponse

from domain import example
from domain.serializers.example_serializer import ExampleSerializer


def example_detail(request, instance_id):
    instance = example.get(instance_id)
    return JsonResponse(
        ExampleSerializer(instance=instance).data
    )
