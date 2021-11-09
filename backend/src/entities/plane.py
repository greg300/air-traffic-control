# coding=utf-8

from sqlalchemy import Column, String
from marshmallow import Schema, fields

from .entity import Entity, Base

class Plane(Entity, Base):
    __tablename__ = 'planes'

    name = Column(String)
    serial_no = Column(String)
    make = Column(String)

    def __init__(self, name, serial_no, make, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.serial_no = serial_no
        self.make = make

class PlaneSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    serial_no = fields.Str()
    make = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()