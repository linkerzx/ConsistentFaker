"""
Fake Base class object
-----------------------------
[TODO PLACEHOLDER]
"""
import uuid
import json


class FakeBaseObject:
    """
    Base Fake Object
    """
    def __init__(self, **kwargs):
        """ Initializing the fake base object"""
        self._uid = self._init_uid(kwargs.get("uid"))

    @property
    def uid(self) -> uuid.UUID:
        """uuid: unique Fake Payment id"""
        return self._uid

    @classmethod
    def to_dict(cls):
        """Not Implemented"""
        return NotImplemented

    def to_json(self):
        """
        Serialize the fake payment object to a json
        """
        return json.dumps(self.to_dict())

    @classmethod
    def _init_uid(cls, uid: uuid.UUID = None) -> uuid.UUID:
        """
        Assign or generate a guid
        Returns:
            uuid.UUID: order item id
        """
        if uid and isinstance(uid, uuid.UUID):
            return uid
        if uid:
            raise TypeError("uid kwarg should be an instance of uuid.UUID")
        return uuid.uuid4()
