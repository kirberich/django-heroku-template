from data.models import TestModel
from rest_framework import serializers


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('id', 'created', 'updated', 'method_field')

    method_field = serializers.SerializerMethodField()

    def get_method_field(self, obj):
        return 'works!'
