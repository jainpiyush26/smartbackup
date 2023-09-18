#!/usr/bin/env python3
# stdlib imports
import os
from jsonschema import validate
# internal imports

# external imports


# custom exception classes
class InputInvalidError(Exception):
    pass


SCHEMA = """
"""


def object_validate(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    # We validate the schema of the object
    validate(object, SCHEMA)

    if not os.path.exists(object.source):
        raise InputInvalidError("Following source folder doesn't exist {object.source}")

    if not os.path.exists(object.destination) and object.create_destination is False:
        raise InputInvalidError("Following destination folder doesn't exist {object.destination}")
    
    