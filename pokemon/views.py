from pokemon.models import Pokemon
from django.db import connection
from pokemon.serializers import PokemonSerializers, PostPokemonSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

error_response = {"API call": "Failed"}

@api_view(['GET'])
def pokemon(request):
    try:
        if request.method == 'GET':
            pokemon = Pokemon.objects.raw("SELECT * FROM pokemon ORDER BY pokedex_no")
            serializer = PokemonSerializers(pokemon, many=True)
            return Response(serializer.data)
    except Exception:
        print("API call error!")
        return Response(error_response)
    
@api_view(['GET'])
def get_fairy_pokemon(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM pokemon WHERE type_1 = 'Fairy' OR type_2 = 'Fairy'")
                        all_fairy_pokemon = cursor.fetchall()
                  list_of_fairy_pokemon = []
                  for pokemon in all_fairy_pokemon:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_fairy_pokemon.append(dictionary)
                  return Response(list_of_fairy_pokemon)
      except Exception:
            print("API call error!")
            return Response(error_response)

@api_view(['GET', 'POST'])
def add_pokemon(request):
    if request.method == 'GET':
        pokemon = Pokemon.objects.all()
        serializer = PokemonSerializers(pokemon, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostPokemonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
         print("API call error!")
         return Response(error_response)

@api_view(['GET'])
def get_legendary_pokemon(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM pokemon WHERE legendary = 'True' \
                                       AND name NOT LIKE '%Mega%'")
                        all_legendary_pokemon = cursor.fetchall()
                  list_of_legendary_pokemon = []
                  for pokemon in all_legendary_pokemon:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_legendary_pokemon.append(dictionary)
                  return Response(list_of_legendary_pokemon)
      except Exception:
            print("API call error!")
            return Response(error_response)

@api_view(['GET'])
def get_top_ten_fastest_pokemon(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT pokedex_no, name, type_1, type_2, \
                                       speed, generation FROM pokemon WHERE legendary = 'False' \
                                       AND name NOT LIKE '%Mega%' ORDER BY speed DESC LIMIT 10")
                        fast_pokemon = cursor.fetchall()
                  list_of_fast_pokemon = []
                  for pokemon in fast_pokemon:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_fast_pokemon.append(dictionary)
                  return Response(list_of_fast_pokemon)
      except Exception:
            print("API call error!")
            return Response(error_response)

@api_view(['GET'])
def get_top_five_weakest_pokemon(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT pokedex_no, name, total FROM pokemon \
                                       ORDER BY total LIMIT 5")
                        weak_pokemon = cursor.fetchall()
                  list_of_weak_pokemon = []
                  for pokemon in weak_pokemon:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_weak_pokemon.append(dictionary)
                  return Response(list_of_weak_pokemon)
      except Exception:
            print("API call error!")
            return Response(error_response)

@api_view(['GET'])
def get_top_three_physical_attacking_pokemon(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM pokemon WHERE legendary = 'False' AND \
                                       name NOT LIKE '%Mega%' ORDER BY attack DESC LIMIT 3")
                        strong_pokemon = cursor.fetchall()
                  list_of_strong_pokemon = []
                  for pokemon in strong_pokemon:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_strong_pokemon.append(dictionary)
                  return Response(list_of_strong_pokemon)
      except Exception:
            print("API call error!")
            return Response(error_response)

@api_view(['GET'])
def get_generation_three_pokemon(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT pokedex_no, name, type_1, type_2, generation, \
                                       legendary FROM pokemon WHERE generation = '3' AND \
                                        name NOT LIKE '%Mega%' AND name NOT LIKE '%Primal%'")
                        generation_three = cursor.fetchall()
                  list_of_generation_three = []
                  for pokemon in generation_three:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_generation_three.append(dictionary)
                  return Response(list_of_generation_three)
      except Exception:
            print("API call error!")
            return Response(error_response)

@api_view(['GET'])
def get_all_mega_pokemon(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT pokedex_no, name, generation, legendary \
                                       FROM pokemon WHERE name LIKE '%Mega%' AND name != 'Meganium'")
                        mega_pokemon = cursor.fetchall()
                  list_of_mega_pokemon = []
                  for pokemon in mega_pokemon:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_mega_pokemon.append(dictionary)
                  return Response(list_of_mega_pokemon)
      except Exception:
            print("API call error!")
            return Response(error_response)

@api_view(['GET'])
def get_all_pokemon_that_start_with_o(request):
      try:
            if request.method == 'GET':
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT name FROM pokemon WHERE name LIKE 'O%'")
                        o_pokemon = cursor.fetchall()
                  list_of_pokemon_that_start_with_o = []
                  for pokemon in o_pokemon:
                        dictionary = {}
                        for i, col in enumerate(cursor.description):
                              dictionary[col[0]] = pokemon[i]
                        list_of_pokemon_that_start_with_o.append(dictionary)
                  return Response(list_of_pokemon_that_start_with_o)
      except Exception:
            print("API call error!")
            return Response(error_response)
