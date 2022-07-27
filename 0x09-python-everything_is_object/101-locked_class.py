#!/usr/bin/python3

class LockedClass:
    """
    This class dynamically prevents the user from creating new
    instance attributes, except if the new instance attribute
    is called name
    """
    __slots__ = ["name"]
