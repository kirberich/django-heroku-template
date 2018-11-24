import pytest

from domain import example


@pytest.mark.django_db
def test_get(example_instance):
    example_instance.save()
    instance = example.get(example_instance.id)
    assert instance == example_instance
