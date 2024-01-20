import pytest
import peewee
from peewee_enum_field import EnumField
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class SampleModel(peewee.Model):
    color = EnumField(Color)

@pytest.fixture(autouse=True)
def test_db(tmpdir):
    db = peewee.SqliteDatabase(tmpdir / "test.db")
    SampleModel._meta.database = db
    db.connect()
    db.create_tables([SampleModel])
    yield db
    db.drop_tables([SampleModel])
    db.close()

def test_create_an_instance_with_valid_enum_member():
    model_instance = SampleModel.create(color=Color.RED)

    assert model_instance.color == Color.RED

def test_cannot_create_an_instance_with_an_implicit_conversion_of_an_enum_member_value():
    with pytest.raises(TypeError):
        SampleModel.create(color=Color.RED.value)

def test_cannot_create_an_instance_with_invalid_enum_member():
    with pytest.raises(TypeError):
        SampleModel.create(color=10)

def test_cannot_create_an_instance_with_a_different_enum():
    class Volume(Enum):
        LOW = 1
        HIGH = 2

    with pytest.raises(TypeError):
        SampleModel.create(color=Volume.LOW)

def test_get_an_enum_from_db():
    SampleModel.create(color=Color.GREEN)

    fetched_instance = SampleModel.get(SampleModel.color == Color.GREEN)

    assert fetched_instance.color == Color.GREEN
