from rest_framework import serializers
from .models import Pokemon, Stat


class StatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = [
            'name',
            'base_stat',
        ]


class PokemonSerializer(serializers.ModelSerializer):
    evolutions = serializers.SerializerMethodField()
    stats = StatSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'stats',
            'height',
            'weight',
            'name',
            'evolutions',
        ]
        deph = 1

    def get_evolutions(self, obj):
        result = []
        child = obj.child

        while child:
            pokemon = {
                'id': child.id,
                'name': child.name,
                'type': 'PREEVOLUTION'
            }
            result.append(pokemon)
            child = child.child

        parent = obj.parent.all().first() if obj.parent else None
        while parent:
            pokemon = {
                'id': parent.id,
                'name': parent.name,
                'type': 'EVOLUTION'
            }
            result.append(pokemon)
            parent = parent.parent.all().first() if parent.parent else None

        return result