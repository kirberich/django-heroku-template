import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_example_detail(example_instance):
    example_instance.save()
    
    client = Client()
    response = client.get(reverse('example-detail', kwargs={'instance_id': example_instance.id}))
    assert response.status_code == 200
