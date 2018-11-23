from data.models import TestModel
from data.models.base_model import BaseModel


def test_test_model():
    instance = TestModel()
    assert isinstance(instance, BaseModel)
