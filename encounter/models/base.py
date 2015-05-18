__author__ = 'it'

class BaseModel(object):
    __name__ = "base"

    def __init__(self, table_name="base", **kwargs):
        BaseModel.__name__ = table_name

        self.fields = kwargs.keys()
        self.fields.append("table_name")
        for k, v in kwargs.items():
            setattr(self, k, v)

    def as_dict(self):
        return dict((field, getattr(self, field, None))
                    for field in self.fields)

    def __eq__(self, other):
        return other.as_dict() == self.as_dict()

    def __hash__(self):
        hash(__name__ + str(self.as_dict().items()))
