from .models import Reaction
from rest_framework import serializers

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = [
            'id', 'reaction', 'reacted_at'
        ]
        read_only_fields = [ 'id', 'reacted_at']
