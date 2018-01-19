# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mongoengine import Document, EmbeddedDocument, fields,DynamicDocument
from war.settings import db

class Battle(DynamicDocument):
    name = fields.StringField()
    year = fields.IntField()
    battle_number = fields.IntField()
    attacker_king = fields.StringField()
    defender_king = fields.StringField()
    attacker_1 = fields.StringField()
    attacker_2 = fields.StringField()
    attacker_3 = fields.StringField()
    attacker_4 = fields.StringField()
    defender_1 = fields.StringField()
    defender_2 = fields.StringField()
    defender_3 = fields.StringField()
    defender_4 = fields.StringField()
    attacker_outcome =fields.StringField()
    battle_type = fields.StringField()
    major_death = fields.IntField()
    major_capture = fields.IntField()
    attacker_size = fields.IntField()
    defender_size = fields.IntField()
    attacker_commander = fields.StringField()
    defender_commander = fields.StringField()
    summer = fields.StringField()
    location = fields.StringField()
    region = fields.StringField()
    note = fields.StringField()     
    meta = {
        'collection': 'battles'
    }

    