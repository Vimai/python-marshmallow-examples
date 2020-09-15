import datetime as dt
from marshmallow import Schema, fields
from pprint import pprint


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


if __name__ == '__main__':
    user = User(name="Monty", email="monty@python.org")
    schema = UserSchema()
    result = schema.dump(user)
    pprint(result)
    json_result = schema.dumps(user)
    pprint(json_result)
    print(type(json_result))

    summary_schema = UserSchema(only=("name", "email"))
    pprint(summary_schema.dump(user))
