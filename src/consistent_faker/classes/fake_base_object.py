"""
Fake Base class object

Copyright (c) 2019 Julien Kervizic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
        if uid and isinstance(uid, str):
            try: 
                uuid_obj = uuid.UUID(uid, version=4)
                return uuid_obj if str(uuid_obj) == uid else None
            except ValueError:
                raise ValueError("uid kwarg str is not a valid uuid.UUIDv4")
        if uid:
            raise TypeError("uid kwarg should be an instance of uuid.UUID")
        return uuid.uuid4()
