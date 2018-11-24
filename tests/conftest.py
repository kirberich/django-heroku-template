import pytest

from data.models import TestModel


@pytest.fixture
def example_instance():
    return TestModel(id=1)
