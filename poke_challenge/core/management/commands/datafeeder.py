from django.core.management import BaseCommand
from core.models import Pokemon, Stat
import requests

POKE_EVOLUTION_CHANGE_URL = 'https://pokeapi.co/api/v2/evolution-chain/{id}/'
POKEMON_URL = 'https://pokeapi.co/api/v2/pokemon/{name}/'


class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument('evolution_chain_id', nargs='+', type=int)

    def handle(self, *args, **options):
        evolution_chain_id = options['evolution_chain_id'][0]

        evolution_chain = requests.get(POKE_EVOLUTION_CHANGE_URL.format(
            id=evolution_chain_id
        ))
        json_chain = evolution_chain.json()
        chain = [json_chain['chain']]
        new_pokemon = None
        while chain:
            child = new_pokemon
            pokemon_name = chain[0]['species']['name']
            pokemon = requests.get(POKEMON_URL.format(
                name=pokemon_name
            ))
            json_pokemon = pokemon.json()
            new_pokemon = Pokemon(
                name=json_pokemon['name'],
                height=json_pokemon['height'],
                weight=json_pokemon['weight'],
                child=child
            )
            new_pokemon.save()
            for stat in json_pokemon['stats']:
                new_stat = Stat(
                    pokemon=new_pokemon,
                    name=stat['stat']['name'],
                    base_stat=stat['base_stat']
                )
                new_stat.save()
            chain = chain[0]['evolves_to']