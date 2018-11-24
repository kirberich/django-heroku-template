from domain.serializers import ExampleSerializer

def test_example_serializer():
    serializer = ExampleSerializer(data={})
    assert serializer.is_valid()
    assert serializer.data['method_field'] == 'works!'
