from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=32)
    discriminator = fields.CharField(max_length=4)
    avatar = fields.CharField(max_length=32, null=True)
    bot = fields.BooleanField(null=True)
    system = fields.BooleanField(null=True)
    flags = fields.BigIntField(null=True)
    premium_type = fields.BigIntField(null=True)
    public_flags = fields.BigIntField(null=True)
