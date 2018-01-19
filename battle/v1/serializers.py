from django.contrib.auth.models import User, Group
from rest_framework import serializers
from battle.models import Battle
from rest_framework_mongoengine.serializers import DocumentSerializer

# class BattleSerializer(DocumentSerializer):
#     class Meta:
#     	model = Battle
#     	serializers = ('name','year','battle_number','attacker_king','defender_king','attacker_1','attacker_2','attacker_3','attacker_4','defender_1','defender_2','defender_3','defender_4','attacker_outcome','battle_type','major_death','major_capture','attacker_size','defender_size','attacker_commander','defender_commander','summer','location','region','note')

# from rest_framework import serializers



class BattleSerializer(serializers.Serializer):

    name = serializers.CharField()
    year = serializers.CharField()
    battle_number = serializers.CharField()
    attacker_king = serializers.CharField()
    defender_king = serializers.CharField()
    attacker_1 = serializers.CharField()
    attacker_2 = serializers.CharField()
    attacker_3 = serializers.CharField()
    attacker_4 = serializers.CharField()
    defender_1 = serializers.CharField()
    defender_2 = serializers.CharField()
    defender_3 = serializers.CharField()
    defender_4 = serializers.CharField()
    attacker_outcome =serializers.CharField()
    battle_type = serializers.CharField()
    major_death = serializers.CharField()
    major_capture = serializers.CharField()
    attacker_size = serializers.CharField()
    defender_size = serializers.CharField()
    attacker_commander = serializers.CharField()
    defender_commander = serializers.CharField()
    summer = serializers.CharField()
    location = serializers.CharField()
    region = serializers.CharField()
    note = serializers.CharField()         

