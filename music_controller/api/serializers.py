"""
Takes a model and trasnlate to JSON response {col: val}
"""

from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Room
        fields = (
            'id',               # PK -> auto defined from models.model
            'code', 
            'host', 
            'guest_can_pause', 
            'votes_to_skip', 
            'created_at'
        ) 
