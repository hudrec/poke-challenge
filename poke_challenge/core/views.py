from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status


# Create your views here.
class SearchView(APIView):

    def get(self, request):
        print('ALTO')
        name = request.GET.get('name')

        pokemon = get_object_or_404(Pokemon, name=name)

        pokemon_serializer = PokemonSerializer(instance=pokemon)
        print(pokemon_serializer.data)
        return Response(data=pokemon_serializer.data)

