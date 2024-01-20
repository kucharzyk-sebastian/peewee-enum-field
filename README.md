# peewee-enum-field

A custom field for [Peewee](http://docs.peewee-orm.com/en/latest/), a small, expressive ORM, that allows for the easy integration of Python Enums in Peewee models.

## Overview

`peewee-enum-field` provides a convenient way to store Python Enum types in a Peewee database. This custom field stores the name of an Enum member as a string in the database and handles automatic conversion between the Enum type and the string representation when reading or writing to the database.

## Installation

To install `peewee-enum-field`, you can use pip:

```bash
pip install peewee-enum-field
```

## Usage

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

Then, use EnumField in your Peewee model:

```python
import peewee
from peewee_enum_field import EnumField

class MyModel(peewee.Model):
    color = EnumField(Color)
```

You can now assign Enum members to the field, filter, etc:

```python
instance = MyModel.create(color=Color.RED)
instance = MyModel.get(Color.color == Color.RED)
```

The field automatically handles conversion to and from the Enum type:

```python
assert instance.color == Color.RED
```


## Features
- Easy integration with Peewee models.
- Stores the name of the Enum member in the database for readability.
- Automatically converts to and from the Python Enum type.

## Requirements
- Python 3.6+
- Peewee

## License
peewee-enum-field is released under the [MIT License](LICENSE).
