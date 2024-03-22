import json


class JsonInterface:
    """
    Make the models.Model able to be converted to JSON
    """

    def to_dict(self):
        obj = {}
        class_fields = self.__class__._meta.get_fields()
        fields = [f.name for f in class_fields]

        for field in fields:
            if not hasattr(self, field):
                continue
            obj[field] = str(getattr(self, field))

        return obj

    def to_json(self, indent=4):
        return json.dumps(self.to_dict(), indent=indent)
